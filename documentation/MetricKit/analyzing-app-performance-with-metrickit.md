# Analyzing app performance with MetricKit

**Framework**: MetricKit

Work with the metric values, diagnostic data, and environments in MetricKit reports.

#### Overview

MetricKit reports contain a rich set of typed measurements, diagnostic data, and environmental context. [`MetricResult`](metricresult.md) carries individual metric values (scalars, histograms, or statistics depending on the metric), and you can use the [`metricGroup`](metricresult/metricgroup.md) property to route them to category-specific handlers. [`DiagnosticReport`](diagnosticreport.md) wraps a single [`DiagnosticResult`](diagnosticresult.md) case with type-specific properties and a [`CallStackTree`](callstacktree.md) you can navigate to locate the code involved. [`MetricReport`](metricreport.md) and [`DiagnosticReport`](diagnosticreport.md) include an environment with device, operating system, and app context. Both also conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable), so you can serialize them with [`JSONEncoder`](https://developer.apple.com/documentation/Foundation/JSONEncoder) for storage or upload.

#### Filter Groups of Metrics

Every [`MetricResult`](metricresult.md) case carries a [`metricGroup`](metricresult/metricgroup.md) property that returns a [`MetricGroup`](metricgroup.md) value identifying the category the measurement belongs to, such as CPU, GPU, memory, or disk I/O. You can use [`metricGroup`](metricresult/metricgroup.md) to filter the [`values`](metricreport/intervalentry/values.md) array without writing an exhaustive switch. This pattern is useful when routing measurements to category-specific handlers, logging only a subset of metrics, or building a summary that groups data by category.

```swift
let memoryValues = entry.values.filter { $0.metricGroup == .memory }
```

#### Understand Measurements

The majority of values are scalar values expressed as a [`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement). A `Measurement` pairs a `Double` value with a unit. MetricKit uses unit types including:

- **[`UnitDuration`](https://developer.apple.com/documentation/Foundation/UnitDuration)**: Time-based measurements such as CPU time, hang time, background activity durations, and launch times.
- **[`UnitInformationStorage`](https://developer.apple.com/documentation/Foundation/UnitInformationStorage)**: Byte-based measurements such as memory usage, network transfer totals, and disk sizes.
- **[`UnitFrequency`](https://developer.apple.com/documentation/Foundation/UnitFrequency)**: Rate measurements such as frames per second in [`MetricResult.metalFrameRate(_:)`](metricresult/metalframerate(_:).md).
- **[`SignalBars`](signalbars.md)**: The [`Dimension`](https://developer.apple.com/documentation/Foundation/Dimension) subclass used in [`MetricResult.cellularConditionTime(_:)`](metricresult/cellularconditiontime(_:).md) histograms to represent cellular signal strength levels.
- **[`HitchTimeRatio`](hitchtimeratio.md)**: The [`Dimension`](https://developer.apple.com/documentation/Foundation/Dimension) subclass used by [`ratio`](hitchtimemetric/ratio.md) and [`hitchTimeRatio`](signpostintervalmetric/hitchtimeratio.md) to represent the ratio of hitch time to total tracked time, expressed as milliseconds per second.

#### Work with Histogram Distributions

Several [`MetricResult`](metricresult.md) cases expose a [`Histogram`](histogram.md) rather than a scalar value. A `Histogram` contains an ordered array of buckets, each with a lower bound, an upper bound, and a count of observations that fell within that range.

Iterating through the buckets gives you the full distribution of measured values:

```swift
case let .hangTime(metric):
    for bucket in metric.histogram.buckets {
        print(
            "\(bucket.lowerBound) – \(bucket.upperBound):"
            + " \(bucket.count) hangs"
        )
    }
```

#### Work with Average Statistics

Some metrics report a single averaged value rather than a distribution. For example, [`SuspendedMemoryMetric`](suspendedmemorymetric.md) exposes a [`value`](suspendedmemorymetric/value.md) property of type [`AverageStatistics`](averagestatistics.md). It provides three properties: an average, a count, and an optional standard deviation. A [`count`](averagestatistics/count.md) of zero means the sample count isn’t available for this reporting period. [`standardDeviation`](averagestatistics/standarddeviation.md) is `nil` when unavailable.

```swift
case let .suspendedMemory(metric):
    let statistics = metric.value
    print("Average suspended memory: \(statistics.average)")

    if statistics.count > 0 {
        // A count equal to 0 means it's unavailable.
        print("Sample count: \(statistics.count)")
    }

    if let standardDeviation = statistics.standardDeviation {
        print("Std dev: \(standardDeviation)")
    }
```

#### Read Location and Disk Space Metrics

Not every metric condenses to a single value. [`MetricResult.locationActivityTime(_:)`](metricresult/locationactivitytime(_:).md) breaks location accuracy usage into six tiers, each a `Measurement<UnitDuration>`:

```swift
case let .locationActivityTime(metric):
    print("Best accuracy for navigation: \(metric.bestAccuracyForNavigation)")
    print("Best accuracy:               \(metric.bestAccuracy)")
    print("Ten meters:                  \(metric.tenMeters)")
    print("One hundred meters:          \(metric.oneHundredMeter)")
    print("One kilometer:               \(metric.oneKilometer)")
    print("Three kilometers:            \(metric.threeKilometers)")
```

[`MetricResult.totalFileCount(_:)`](metricresult/totalfilecount(_:).md) and [`MetricResult.totalFileSize(_:)`](metricresult/totalfilesize(_:).md) distinguish binary content from data content. Use them to understand how your app’s storage breaks down between executable code and user data:

```swift
case let .totalFileSize(metric):
    print("Binary size: \(metric.binaryFileSize)")
    print("Data size:   \(metric.dataFileSize)")

case let .totalFileCount(metric):
    print("Binary files: \(metric.binaryFileCount)")
    print("Data files:   \(metric.dataFileCount)")

case let .totalDiskSpaceCapacity(metric):
    print("Device capacity: \(metric.capacity)")
```

[`MetricResult.metalFrameRate(_:)`](metricresult/metalframerate(_:).md) provides frame statistics for a specific Metal layer, including the layer name, frame count, active drawing duration, and a frames-per-second measurement:

```swift
case let .metalFrameRate(metric):
    print("Layer: \(metric.layerName)")
    print("Frames: \(metric.frameCount)")
    print("Active drawing: \(metric.activeDrawingDuration)")
    print("FPS: \(metric.framesPerSecond)")
```

#### Extract Diagnostic Details

Each [`DiagnosticReport`](diagnosticreport.md) wraps a single [`DiagnosticResult`](diagnosticresult.md) case. Switch over the result to access the type-specific properties of each diagnostic. MetricKit generates a [`MemoryExceptionDiagnostic`](memoryexceptiondiagnostic.md) when your app or extension terminates because it exceeds the memory limit.  [`MemoryExceptionDiagnostic`](memoryexceptiondiagnostic.md) is only available on iOS.

```swift
switch report.result {
case let .crash(diagnostic):
    if let reason = diagnostic.terminationReason {
        log("Termination reason: \(reason.rawValue)")
    }
    if let exceptionType = diagnostic.exceptionType {
        log("Exception type: \(exceptionType)")
    }
    analyze(diagnostic.callStackTree)
case let .hang(diagnostic):
    log("Hang duration: \(diagnostic.hangDuration)")
    analyze(diagnostic.callStackTree)
case let .cpuException(diagnostic):
    log("CPU time: \(diagnostic.totalCPUTime)")
    log("Sampled time: \(diagnostic.totalSampledTime)")
    analyze(diagnostic.callStackTree)
case let .diskWriteException(diagnostic):
    log("Bytes written: \(diagnostic.totalBytesWritten)")
    analyze(diagnostic.callStackTree)
case let .appLaunch(diagnostic):
    log("Launch duration: \(diagnostic.launchDuration)")
case let .memoryException(diagnostic):
    analyze(diagnostic.callStackTree)
@unknown default:
    break
}
```

#### Navigate Call Stack Trees

[`CallStackTree`](callstacktree.md) is the primary structure for analyzing crashes, hangs, and exceptions. It contains an array of [`CallStackThread`](callstackthread.md) values and supports binary metadata lookup by UUID.

The [`callStackPerThread`](callstacktree/callstackperthread.md) property tells you how the frames are organized. When [`callStackPerThread`](callstacktree/callstackperthread.md) is `true`, each thread has its own root frames. When it’s `false`, all frames across all threads are merged into a single thread.

The simplest way to iterate through every frame in the tree is [`forEachFrame(_:)`](callstacktree/foreachframe(_:).md), which handles the recursive [`subFrames`](callstackframe/subframes.md) traversal for you:

```swift
var frames: [(address: UInt64, binaryName: String)] = []

diagnostic.callStackTree.forEachFrame { frame in
    guard let address = frame.address,
          let uuid = frame.binaryUUID,
          let info = diagnostic.callStackTree.binaryInfo[uuid]
    else { return }
    frames.append((address: address, binaryName: info.name))
}
```

[`binaryInfo`](callstacktree/binaryinfo-swift.property.md) is a dictionary, and the key is the same [`binaryUUID`](callstackframe/binaryuuid.md) that each [`CallStackFrame`](callstackframe.md) carries. A [`CallStackTree.BinaryInfo`](callstacktree/binaryinfo-swift.struct.md) value provides the binary’s [`uuid`](callstacktree/binaryinfo-swift.struct/uuid.md) and [`name`](callstacktree/binaryinfo-swift.struct/name.md).

When you need to examine threads individually — for example, to identify the crashing thread separately — iterate [`callStackThreads`](callstacktree/callstackthreads.md) directly. Each [`CallStackThread`](callstackthread.md) exposes a [`rootFrames`](callstackthread/rootframes.md) array, and each [`CallStackFrame`](callstackframe.md) has a [`subFrames`](callstackframe/subframes.md) array for manual recursion:

```swift
for frame in frames {
    if let uuid = frame.binaryUUID,
       let info = tree.binaryInfo[uuid] {
        let indent = String(repeating: "  ", count: depth)
        print("\(indent)\(info.name) + "
            + "\(frame.offsetIntoBinaryTextSegment ?? 0)")
    }
    visitFrames(frame.subFrames, depth: depth + 1, tree: tree)
}
```

#### Review a Reports Environment

[`MetricReport`](metricreport.md) and [`DiagnosticReport`](diagnosticreport.md) both carry an environment that provides context about the device and session at the time of collection. The two environments have different optionality: [`environment`](metricreport/environment-swift.property.md) is optional, while [`environment`](diagnosticreport/environment-swift.property.md) is required.

[`MetricReport.Environment`](metricreport/environment-swift.struct.md) includes [`osVersion`](metricreport/environment-swift.struct/osversion.md), [`deviceType`](metricreport/environment-swift.struct/devicetype.md), [`regionFormat`](metricreport/environment-swift.struct/regionformat.md), and [`lowPowerModeEnabled`](metricreport/environment-swift.struct/lowpowermodeenabled.md). It also exposes [`hasExceededStateLimit`](metricreport/environment-swift.struct/hasexceededstatelimit.md), which is `true` when the number of unique states during the reporting period exceeded the system limit — some state data is then folded into the full-day interval entry rather than appearing in [`stateEntries`](metricreport/stateentries.md).

[`DiagnosticReport.Environment`](diagnosticreport/environment-swift.struct.md) provides additional app-specific context. Check it to understand the exact build context of a diagnostic event:

```swift
let environment = report.environment
print("OS: \(environment.osVersion), device: \(environment.deviceType)")
print("App: \(environment.applicationVersion) (\(environment.applicationBuildVersion))")

if environment.isTestFlightApp {
    print("Running under TestFlight")
}

if !environment.signpostData.isEmpty {
    print("Active signposts at event time:")
    for record in environment.signpostData {
        print("  \(record)")
    }
}
```

[`signpostData`](diagnosticreport/environment-swift.struct/signpostdata.md) is an array of [`SignpostRecord`](signpostrecord.md) values representing any [`OSSignposter`](https://developer.apple.com/documentation/os/OSSignposter) intervals that were active when the diagnostic occurred. [`DiagnosticReport.Environment`](diagnosticreport/environment-swift.struct.md) also provides a [`pid`](diagnosticreport/environment-swift.struct/pid.md), [`bundleIdentifier`](diagnosticreport/environment-swift.struct/bundleidentifier.md), [`regionFormat`](diagnosticreport/environment-swift.struct/regionformat.md), and [`states`](diagnosticreport/environment-swift.struct/states.md).

#### Serialize Reports

Both [`MetricReport`](metricreport.md) and [`DiagnosticReport`](diagnosticreport.md) conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable). To send a [`MetricReport`](metricreport.md) to your server, encode it inside your observation loop using [`JSONEncoder`](https://developer.apple.com/documentation/Foundation/JSONEncoder). Setting the [`encodingFormatKey`](metricreport/encodingformatkey.md) in the encoder’s [`userInfo`](https://developer.apple.com/documentation/Foundation/JSONEncoder/userInfo) to [`MetricReport.EncodingFormat.byStateReportingDomain`](metricreport/encodingformat/bystatereportingdomain.md) groups the encoded output by domain, so both state entries and interval entries in the resulting JSON contain your app’s performance metrics organized by each reporting domain and the states within it:

```swift
import MetricKit

for await report in manager.metricReports {
    do {
        let encoder = JSONEncoder()
        encoder.outputFormatting = .prettyPrinted

        let formatKey = MetricReport.encodingFormatKey
        encoder.userInfo[formatKey] = MetricReport.EncodingFormat.byStateReportingDomain

        let jsonData = try encoder.encode(report)
        // Send to server
    } catch {
        // Handle encoding error
    }
}
```

## See Also

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)
  Receive daily performance and diagnostic reports from real device usage.
- [Track performance by app state using MetricKit](track-performance-by-app-state-using-metrickit.md)
  Collect performance metrics, diagnostic reports, and experiment data related to your app’s current state using the MetricKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/analyzing-app-performance-with-metrickit)*
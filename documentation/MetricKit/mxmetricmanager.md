# MXMetricManager

**Framework**: MetricKit  
**Kind**: class

The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXMetricManager
```

#### Overview

The `MXMetricManager` shared object manages your subscription for receiving on-device daily metrics. It receives daily metric reports when the device your app is installed on is running iOS 13 and later or macOS 26 and later.

MetricKit starts accumulating reports for your app after calling [`shared`](mxmetricmanager/shared.md) for the first time. To receive the reports, call [`add(_:)`](mxmetricmanager/add(_:).md) with an object that adopts the [`MXMetricManagerSubscriber`](mxmetricmanagersubscriber.md) protocol. The system delivers metric reports at most once per day per metric source, and diagnostic reports immediately in iOS 15 and later and macOS 12 and later. Some metrics originate from different system sources and arrive in a separate payload, so your app may receive more than one metric payload per day. The reports contain the metrics from the past 24 hours and any previously undelivered daily reports. To pause receiving reports, call [`remove(_:)`](mxmetricmanager/remove(_:).md).

Calls to add a subscriber and to receive reports are safe to use in performance-sensitive code, such as during app launch.

The following example shows a class that subscribes to and receives MetricKit reports.

```swift
class AppMetrics: NSObject, MXMetricManagerSubscriber {
    func receiveReports() {
       let manager = MXMetricManager.shared
       manager.add(self)
    }

    func pauseReports() {
       let manager = MXMetricManager.shared
       manager.remove(self)
    }

    // Receive daily metrics.
    func didReceive(_ payloads: [MXMetricPayload]) {
       // Process metrics.
    }

    // Receive diagnostics immediately when available.
    func didReceive(_ payloads: [MXDiagnosticPayload]) {
       // Process diagnostics.
    }
}

```

> **Note**: To test MetricKit in your app, run your app on a physical device to receive metric reports and `didReceive(_:)` callbacks.

## Topics

### Getting the shared metrics manager
- [class var shared: MXMetricManager](mxmetricmanager/shared.md)
  An object that returns the shared metrics manager instance.
### Subscribing to reports
- [func add(any MXMetricManagerSubscriber)](mxmetricmanager/add(_:).md)
  Registers to receive a daily report of app metrics from the metrics manager.
- [func remove(any MXMetricManagerSubscriber)](mxmetricmanager/remove(_:).md)
  Unsubscribes from daily reports of app metrics.
### Retrieving previous reports
- [var pastPayloads: [MXMetricPayload]](mxmetricmanager/pastpayloads.md)
  Returns an array of the daily metrics reports generated since the last allocation of the shared manager instance.
- [var pastDiagnosticPayloads: [MXDiagnosticPayload]](mxmetricmanager/pastdiagnosticpayloads.md)
  The diagnostic reports since the last initialization of the shared manager instance.
### Creating custom metric logs
- [class func makeLogHandle(category: String) -> OSLog](mxmetricmanager/makeloghandle(category:).md)
  Returns a log handle used for writing custom metric events.
### Measuring an extended launch
- [class func extendLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](mxmetricmanager/extendlaunchmeasurement(fortaskid:).md)
  Starts to measure an extended launch task with the given task identifier.
- [class func finishExtendedLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](mxmetricmanager/finishextendedlaunchmeasurement(fortaskid:).md)
  Signals the end of an extended launch task.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MXMetricPayload](mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [class MXDiagnosticPayload](mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.
- [protocol MXMetricManagerSubscriber](mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager)*
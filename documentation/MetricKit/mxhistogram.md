# MXHistogram

**Framework**: MetricKit  
**Kind**: class

An object representing a histogram of data values of the same type of unit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXHistogram<UnitType> where UnitType : Unit
```

#### Overview

A  measures the number of times a data point for a variable falls into a specific range of possible values within a set of data. Usually, histograms are depicted as bar charts, in which each bar represents a range of values, and the height of each bar represents the number of times the value of the variable falls within a particular range. In this class, each bar is represented by a .

A bucket holds the results for a series of measured values, such as all the events occurring between 3 and 5 seconds. MetricKit uses fixed-width buckets that are device-independent with intervals that are based on the type of metric. Use the [`bucketStart`](mxhistogrambucket/bucketstart.md) and [`bucketEnd`](mxhistogrambucket/bucketend.md) properties to find the start and end of an interval.

The returned results contain only buckets with at least one item so [`bucketEnumerator`](mxhistogram/bucketenumerator.md) may not return all intervals.

For example, if the fixed width for the time to resume the app is 10 ms, then the sequence of buckets is:

0…9 ms, 10…19 ms, 20…29 ms, etc.

If there’s data only in the 0…9 ms and 20…29 ms buckets, then the report skips the 10…19 ms bucket.

## Topics

### Reading the buckets
- [var bucketEnumerator: NSEnumerator](mxhistogram/bucketenumerator.md)
  An enumerator for the buckets containing the data in the histogram.
- [var totalBucketCount: Int](mxhistogram/totalbucketcount.md)
  The total number of buckets in the histogram.
- [class MXHistogramBucket](mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhistogram)*
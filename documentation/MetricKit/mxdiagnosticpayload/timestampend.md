# timeStampEnd

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The ending time of the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.3
- iPadOS 14.0+ - Deprecated in 27.3
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Use [`timeRange`](../diagnosticreport/timerange.md) instead.

## Declaration

```swift
var timeStampEnd: Date { get }
```

```objc
@property (strong, readonly, nonnull) NSDate * timeStampEnd;
```

## See Also

### Reading information about the payload
- [var timeStampBegin: Date](./timestampbegin.md)
  The starting time of the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload/timestampend)*
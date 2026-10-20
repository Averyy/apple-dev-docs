# NEFilterReport.Frequency

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents the frequency of filter report delivery.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
enum Frequency
```

```c
enum NEFilterReportFrequency : NSInteger;
```

## Topics

### Report frequencies
- [NEFilterReport.Frequency.none](./frequency/none.md)
  A frequency value that indicates no report delivery.
- [NEFilterReport.Frequency.low](./frequency/low.md)
  A low frequency of reports, about once every five seconds.
- [NEFilterReport.Frequency.medium](./frequency/medium.md)
  A low frequency of reports, about once every second.
- [NEFilterReport.Frequency.high](./frequency/high.md)
  A low frequency of reports, about once every half-second.
### Initializers
- [init?(rawValue: Int)](./frequency/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting new flow verdict properties
- [var statisticsReportFrequency: NEFilterReport.Frequency](../nefilternewflowverdict/statisticsreportfrequency.md)
  The frequency at which the data provider receives reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/frequency)*
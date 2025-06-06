# NEFilterReport.Frequency

**Framework**: Network Extension  
**Kind**: enum

An enumeration that represents the frequency of filter report delivery.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
enum Frequency
```

## Topics

### Report frequencies
- [NEFilterReport.Frequency.none](nefilterreport/frequency/none.md)
  A frequency value that indicates no report delivery.
- [NEFilterReport.Frequency.low](nefilterreport/frequency/low.md)
  A low frequency of reports, about once every five seconds.
- [NEFilterReport.Frequency.medium](nefilterreport/frequency/medium.md)
  A low frequency of reports, about once every second.
- [NEFilterReport.Frequency.high](nefilterreport/frequency/high.md)
  A low frequency of reports, about once every half-second.
### Initializers
- [init?(rawValue: Int)](nefilterreport/frequency/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var statisticsReportFrequency: NEFilterReport.Frequency](nefilternewflowverdict/statisticsreportfrequency.md)
  The frequency at which the data provider receives reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/frequency)*
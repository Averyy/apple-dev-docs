# fullDayEntry

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The full day interval entry spanning the entire report collection period.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var fullDayEntry: MetricReport.IntervalEntry { get }
```

Available when `Element` is `MetricReport.IntervalEntry`.

#### Discussion

This entry contains metrics aggregated across the entire aggregation period while other interval entries represent breakdowns within that period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/fulldayentry)*
# byStateReportingDomain

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

All states from all interval entries grouped by their StateReporting domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var byStateReportingDomain: [StateReportingDomain : [MetricManager.ReportedState]] { get }
```

Available when `Element` is `MetricReport.IntervalEntry`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/bystatereportingdomain-7plu4)*
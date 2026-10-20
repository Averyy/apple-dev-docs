# daySummary

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The summary of all exposures for the day.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var daySummary: ENExposureSummaryItem { get }
```

```objc
@property (nonatomic, strong, readonly) ENExposureSummaryItem * daySummary;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

### Getting Exposure Summary Information
- [var date: Date](./date.md)
  The date that the exposure occurred.
- [var confirmedClinicalDiagnosisSummary: ENExposureSummaryItem?](./confirmedclinicaldiagnosissummary.md)
  The summary of exposures from a clinically-originated diagnosis.
- [var confirmedTestSummary: ENExposureSummaryItem?](./confirmedtestsummary.md)
  The summary of exposures with a confirmed diagnosis.
- [var recursiveSummary: ENExposureSummaryItem?](./recursivesummary.md)
  The summary of exposures that came from someone else who was exposed.
- [var selfReportedSummary: ENExposureSummaryItem?](./selfreportedsummary.md)
  The summary of self-reported exposures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredaysummary/daysummary)*
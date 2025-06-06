# daySummary

**Framework**: Exposure Notification  
**Kind**: property

The summary of all exposures for the day.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var daySummary: ENExposureSummaryItem { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

 This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

- [var date: Date](enexposuredaysummary/date.md)
  The date that the exposure occurred.
- [var confirmedClinicalDiagnosisSummary: ENExposureSummaryItem?](enexposuredaysummary/confirmedclinicaldiagnosissummary.md)
  The summary of exposures from a clinically-originated diagnosis.
- [var confirmedTestSummary: ENExposureSummaryItem?](enexposuredaysummary/confirmedtestsummary.md)
  The summary of exposures with a confirmed diagnosis.
- [var recursiveSummary: ENExposureSummaryItem?](enexposuredaysummary/recursivesummary.md)
  The summary of exposures that came from someone else who was exposed.
- [var selfReportedSummary: ENExposureSummaryItem?](enexposuredaysummary/selfreportedsummary.md)
  The summary of self-reported exposures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredaysummary/daysummary)*
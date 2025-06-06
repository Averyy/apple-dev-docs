# ENExposureDaySummary

**Framework**: Exposure Notification  
**Kind**: class

The summary of exposure information for a single day.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENExposureDaySummary
```

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, and in iOS 13.7 and later.

 This class is available in iOS 12.5, and in iOS 13.7 and later.

## Topics

### Getting Exposure Summary Information
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
- [var daySummary: ENExposureSummaryItem](enexposuredaysummary/daysummary.md)
  The summary of all exposures for the day.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ENExposureDetectionSummary](enexposuredetectionsummary.md)
  A summary of exposures.
- [class ENExposureSummaryItem](enexposuresummaryitem.md)
  The summary of exposures for a specific time period or report type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredaysummary)*
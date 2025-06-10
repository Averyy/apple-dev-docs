# ENExposureDetectionSummary

**Framework**: Exposure Notification  
**Kind**: class

A summary of exposures.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENExposureDetectionSummary
```

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### Exposure Criteria
- [var attenuationDurations: [NSNumber]](enexposuredetectionsummary/attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var daysSinceLastExposure: Int](enexposuredetectionsummary/dayssincelastexposure.md)
  Number of days since the most recent exposure.
- [var matchedKeyCount: UInt64](enexposuredetectionsummary/matchedkeycount.md)
  The number of keys that matched for an exposure detection.
- [var maximumRiskScore: ENRiskScore](enexposuredetectionsummary/maximumriskscore.md)
  The vaue that represents the highest risk score of all exposure incidents.
- [var maximumRiskScoreFullRange: Double](enexposuredetectionsummary/maximumriskscorefullrange.md)
  The value that represents the highest, full-range risk score of all the exposures for the user.
- [var riskScoreSumFullRange: Double](enexposuredetectionsummary/riskscoresumfullrange.md)
  The sum of the full-range risk scores for all exposures for the user.
- [var metadata: [AnyHashable : Any]?](enexposuredetectionsummary/metadata.md)
  The metadata associated with the summary.
- [var daySummaries: [ENExposureDaySummary]](enexposuredetectionsummary/daysummaries.md)
  The summary of each day that contains an exposure.

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

- [class ENExposureDaySummary](enexposuredaysummary.md)
  The summary of exposure information for a single day.
- [class ENExposureSummaryItem](enexposuresummaryitem.md)
  The summary of exposures for a specific time period or report type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary)*
# metadata

**Framework**: Exposure Notification  
**Kind**: property

The metadata associated with the summary.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var metadata: [AnyHashable : Any]? { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

Not used.

## See Also

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
- [var daySummaries: [ENExposureDaySummary]](enexposuredetectionsummary/daysummaries.md)
  The summary of each day that contains an exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/metadata)*
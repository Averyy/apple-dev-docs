# daySummaries

**Framework**: Exposure Notification  
**Kind**: property

The summary of each day that contains an exposure.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var daySummaries: [ENExposureDaySummary] { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

Day summaries are only available in apps specifying an `ENAPIVersion` of 2 in their Info.plist.

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
- [var metadata: [AnyHashable : Any]?](enexposuredetectionsummary/metadata.md)
  The metadata associated with the summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/daysummaries)*
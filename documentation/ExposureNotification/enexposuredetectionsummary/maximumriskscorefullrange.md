# maximumRiskScoreFullRange

**Framework**: Exposure Notification  
**Kind**: property

The value that represents the highest, full-range risk score of all the exposures for the user.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var maximumRiskScoreFullRange: Double { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.6 and later.

 This property is available in iOS 12.5, and in iOS 13.6 and later.

This value is not limited by [`ENRiskScoreMax`](enriskscoremax.md).

> **Note**:  This value is only available when `ENAPIVersion` is set to `1` in the app’s Info.plist file.

 This value is only available when `ENAPIVersion` is set to `1` in the app’s Info.plist file.

## See Also

- [var attenuationDurations: [NSNumber]](enexposuredetectionsummary/attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var daysSinceLastExposure: Int](enexposuredetectionsummary/dayssincelastexposure.md)
  Number of days since the most recent exposure.
- [var matchedKeyCount: UInt64](enexposuredetectionsummary/matchedkeycount.md)
  The number of keys that matched for an exposure detection.
- [var maximumRiskScore: ENRiskScore](enexposuredetectionsummary/maximumriskscore.md)
  The vaue that represents the highest risk score of all exposure incidents.
- [var riskScoreSumFullRange: Double](enexposuredetectionsummary/riskscoresumfullrange.md)
  The sum of the full-range risk scores for all exposures for the user.
- [var metadata: [AnyHashable : Any]?](enexposuredetectionsummary/metadata.md)
  The metadata associated with the summary.
- [var daySummaries: [ENExposureDaySummary]](enexposuredetectionsummary/daysummaries.md)
  The summary of each day that contains an exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/maximumriskscorefullrange)*
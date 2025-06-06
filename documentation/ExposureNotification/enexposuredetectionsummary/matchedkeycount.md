# matchedKeyCount

**Framework**: Exposure Notification  
**Kind**: property

The number of keys that matched for an exposure detection.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var matchedKeyCount: UInt64 { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

The framework computes this property’s value across all matching exposures, not just exposures that meet or exceed [`minimumRiskScore`](enexposureconfiguration/minimumriskscore.md) or [`minimumRiskScoreFullRange`](enexposureconfiguration/minimumriskscorefullrange.md).

This value is only available when `ENAPIVersion` is set to `1` in the app’s `Info.plist` file.

## See Also

- [var attenuationDurations: [NSNumber]](enexposuredetectionsummary/attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var daysSinceLastExposure: Int](enexposuredetectionsummary/dayssincelastexposure.md)
  Number of days since the most recent exposure.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/matchedkeycount)*
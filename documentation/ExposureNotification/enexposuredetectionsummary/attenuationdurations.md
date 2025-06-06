# attenuationDurations

**Framework**: Exposure Notification  
**Kind**: property

An array of durations at specific radio signal attenuations.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var attenuationDurations: [NSNumber] { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

An array that contains the duration, in seconds, at certain attenuations, using an aggregated maximum exposures of 30 minutes.

`array[0]` =  Sum of durations for all exposures when attenuation value was `A <= X`.

`array[1]` =  Sum of durations for all exposures when attenuation value was `X < A <= Y`.

`array[2]` =  Sum of durations for all exposures when attenuation value was `Y < A`.

Use the [`attenuationDurationThresholds`](enexposureconfiguration/attenuationdurationthresholds.md) to configure the `X` and `Y` values.

> **Note**:  This value is only available when `ENAPIVersion` is set to `1` in the app’s Info.plist file.

 This value is only available when `ENAPIVersion` is set to `1` in the app’s Info.plist file.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/attenuationdurations)*
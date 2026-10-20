# maximumRiskScoreFullRange

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The value that represents the highest, full-range risk score of all the exposures for the user.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var maximumRiskScoreFullRange: Double { get }
```

```objc
@property (nonatomic, assign, readonly) double maximumRiskScoreFullRange;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.6 and later.

This value is not limited by [`ENRiskScoreMax`](../enriskscoremax.md).

> **Note**:  This value is only available when `ENAPIVersion` is set to `1` in the app’s Info.plist file.

## See Also

### Exposure Criteria
- [var attenuationDurations: [NSNumber]](./attenuationdurations.md)
  An array of durations at specific radio signal attenuations.
- [var daysSinceLastExposure: Int](./dayssincelastexposure.md)
  Number of days since the most recent exposure.
- [var matchedKeyCount: UInt64](./matchedkeycount.md)
  The number of keys that matched for an exposure detection.
- [var maximumRiskScore: ENRiskScore](./maximumriskscore.md)
  The vaue that represents the highest risk score of all exposure incidents.
- [var riskScoreSumFullRange: Double](./riskscoresumfullrange.md)
  The sum of the full-range risk scores for all exposures for the user.
- [var metadata: [AnyHashable : Any]?](./metadata.md)
  The metadata associated with the summary.
- [var daySummaries: [ENExposureDaySummary]](./daysummaries.md)
  The summary of each day that contains an exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/maximumriskscorefullrange)*
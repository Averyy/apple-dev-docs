# daySummaries

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The summary of each day that contains an exposure.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var daySummaries: [ENExposureDaySummary] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<ENExposureDaySummary *> * daySummaries;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

Day summaries are only available in apps specifying an `ENAPIVersion` of 2 in their Info.plist.

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
- [var maximumRiskScoreFullRange: Double](./maximumriskscorefullrange.md)
  The value that represents the highest, full-range risk score of all the exposures for the user.
- [var riskScoreSumFullRange: Double](./riskscoresumfullrange.md)
  The sum of the full-range risk scores for all exposures for the user.
- [var metadata: [AnyHashable : Any]?](./metadata.md)
  The metadata associated with the summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary/daysummaries)*
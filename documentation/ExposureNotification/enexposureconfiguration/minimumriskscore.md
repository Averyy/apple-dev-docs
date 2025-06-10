# minimumRiskScore

**Framework**: Exposure Notification  
**Kind**: property

The value that is the user’s minimum risk score.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var minimumRiskScore: ENRiskScore { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

The framework excludes exposure incidents with scores lower than the value of this property. There is no default minimum value for this property.

The framework doesn’t use this property when calculating [`matchedKeyCount`](enexposuredetectionsummary/matchedkeycount.md) or [`daysSinceLastExposure`](enexposuredetectionsummary/dayssincelastexposure.md).

## See Also

- [var minimumRiskScoreFullRange: Double](enexposureconfiguration/minimumriskscorefullrange.md)
  The value that is the user’s full-range minimum risk score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/minimumriskscore)*
# minimumRiskScore

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The value that is the user’s minimum risk score.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var minimumRiskScore: ENRiskScore { get set }
```

```objc
@property (nonatomic, assign, readwrite) ENRiskScore minimumRiskScore;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

The framework excludes exposure incidents with scores lower than the value of this property. There is no default minimum value for this property.

The framework doesn’t use this property when calculating [`matchedKeyCount`](../enexposuredetectionsummary/matchedkeycount.md) or [`daysSinceLastExposure`](../enexposuredetectionsummary/dayssincelastexposure.md).

## See Also

### Minimum Threshold Configuration
- [var minimumRiskScoreFullRange: Double](./minimumriskscorefullrange.md)
  The value that is the user’s full-range minimum risk score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/minimumriskscore)*
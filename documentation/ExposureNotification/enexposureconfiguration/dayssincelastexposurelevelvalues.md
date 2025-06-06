# daysSinceLastExposureLevelValues

**Framework**: Exposure Notification  
**Kind**: property

The level values for days since last exposure.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var daysSinceLastExposureLevelValues: [NSNumber] { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

This property contains eight levels, one for each range of days since last exposure:

- `daysSinceLastExposureScores[0]` when days >= 14.
- `daysSinceLastExposureScores[1]` when days >= 12.
- `daysSinceLastExposureScores[2]` when days >= 10.
- `daysSinceLastExposureScores[3]` when days >= 8.
- `daysSinceLastExposureScores[4]` when days >= 6.
- `daysSinceLastExposureScores[5]` when days >= 4.
- `daysSinceLastExposureScores[6]` when days >= 2.
- `daysSinceLastExposureScores[7]` when days >= 0.

## See Also

- [var attenuationDurationThresholds: [NSNumber]](enexposureconfiguration/attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var attenuationLevelValues: [NSNumber]](enexposureconfiguration/attenuationlevelvalues.md)
  The level values for attenuation.
- [var durationLevelValues: [NSNumber]](enexposureconfiguration/durationlevelvalues.md)
  The level values for duration.
- [var transmissionRiskLevelValues: [NSNumber]](enexposureconfiguration/transmissionrisklevelvalues.md)
  The level values for transmission risk.
- [var metadata: [AnyHashable : Any]?](enexposureconfiguration/metadata.md)
  The metadata you use to configure the exposure calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/dayssincelastexposurelevelvalues)*
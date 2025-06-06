# metadata

**Framework**: Exposure Notification  
**Kind**: property

The metadata you use to configure the exposure calculations.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var metadata: [AnyHashable : Any]? { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

Not used.

## See Also

- [var attenuationDurationThresholds: [NSNumber]](enexposureconfiguration/attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var attenuationLevelValues: [NSNumber]](enexposureconfiguration/attenuationlevelvalues.md)
  The level values for attenuation.
- [var daysSinceLastExposureLevelValues: [NSNumber]](enexposureconfiguration/dayssincelastexposurelevelvalues.md)
  The level values for days since last exposure.
- [var durationLevelValues: [NSNumber]](enexposureconfiguration/durationlevelvalues.md)
  The level values for duration.
- [var transmissionRiskLevelValues: [NSNumber]](enexposureconfiguration/transmissionrisklevelvalues.md)
  The level values for transmission risk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/metadata)*
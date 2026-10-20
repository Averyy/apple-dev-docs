# durationLevelValues

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The level values for duration.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var durationLevelValues: [NSNumber] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSArray<NSNumber *> * durationLevelValues;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

This property contains eight levels, each defining a range of exposure duration:

- `durationScores[0]` when duration equals 0.
- `durationScores[1]` when duration <= 5.
- `durationScores[2]` when duration <= 10.
- `durationScores[3]` when duration <= 15.
- `durationScores[4]` when duration <= 20.
- `durationScores[5]` when duration <= 25.
- `durationScores[6]` when duration <= 30.
- `durationScores[7]` when duration  > 30.

## See Also

### Level Configuration
- [var attenuationDurationThresholds: [NSNumber]](./attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var attenuationLevelValues: [NSNumber]](./attenuationlevelvalues.md)
  The level values for attenuation.
- [var daysSinceLastExposureLevelValues: [NSNumber]](./dayssincelastexposurelevelvalues.md)
  The level values for days since last exposure.
- [var transmissionRiskLevelValues: [NSNumber]](./transmissionrisklevelvalues.md)
  The level values for transmission risk.
- [var metadata: [AnyHashable : Any]?](./metadata.md)
  The metadata you use to configure the exposure calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/durationlevelvalues)*
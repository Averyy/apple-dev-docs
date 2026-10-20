# metadata

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The metadata you use to configure the exposure calculations.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var metadata: [AnyHashable : Any]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary * metadata;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

Not used.

## See Also

### Level Configuration
- [var attenuationDurationThresholds: [NSNumber]](./attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var attenuationLevelValues: [NSNumber]](./attenuationlevelvalues.md)
  The level values for attenuation.
- [var daysSinceLastExposureLevelValues: [NSNumber]](./dayssincelastexposurelevelvalues.md)
  The level values for days since last exposure.
- [var durationLevelValues: [NSNumber]](./durationlevelvalues.md)
  The level values for duration.
- [var transmissionRiskLevelValues: [NSNumber]](./transmissionrisklevelvalues.md)
  The level values for transmission risk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/metadata)*
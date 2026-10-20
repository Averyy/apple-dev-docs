# daysSinceLastExposureThreshold

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The number of days to consider when calculating the risk level.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var daysSinceLastExposureThreshold: Int { get set }
```

```objc
@property (nonatomic, assign, readwrite) NSInteger daysSinceLastExposureThreshold;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

The default value is 0, meaning no filtering is applied.

## See Also

### Configuring Duration
- [var attenuationDurationThresholds: [NSNumber]](./attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var immediateDurationWeight: Double](./immediatedurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at immediate distance.
- [var mediumDurationWeight: Double](./mediumdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at medium distance.
- [var nearDurationWeight: Double](./neardurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at close distance.
- [var otherDurationWeight: Double](./otherdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at a large distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/dayssincelastexposurethreshold)*
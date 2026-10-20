# mediumDurationWeight

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The weight assigned to a risk level indicating the duration of the user’s exposure at medium distance.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var mediumDurationWeight: Double { get set }
```

```objc
@property (nonatomic, assign, readwrite) double mediumDurationWeight;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

### Configuring Duration
- [var attenuationDurationThresholds: [NSNumber]](./attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var immediateDurationWeight: Double](./immediatedurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at immediate distance.
- [var nearDurationWeight: Double](./neardurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at close distance.
- [var otherDurationWeight: Double](./otherdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at a large distance.
- [var daysSinceLastExposureThreshold: Int](./dayssincelastexposurethreshold.md)
  The number of days to consider when calculating the risk level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/mediumdurationweight)*
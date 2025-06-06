# daysSinceLastExposureThreshold

**Framework**: Exposure Notification  
**Kind**: property

The number of days to consider when calculating the risk level.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var daysSinceLastExposureThreshold: Int { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

 This property is available in iOS 12.5, and in iOS 13.7 and later.

The default value is 0, meaning no filtering is applied.

## See Also

- [var attenuationDurationThresholds: [NSNumber]](enexposureconfiguration/attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var immediateDurationWeight: Double](enexposureconfiguration/immediatedurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at immediate distance.
- [var mediumDurationWeight: Double](enexposureconfiguration/mediumdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at medium distance.
- [var nearDurationWeight: Double](enexposureconfiguration/neardurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at close distance.
- [var otherDurationWeight: Double](enexposureconfiguration/otherdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at a large distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/dayssincelastexposurethreshold)*
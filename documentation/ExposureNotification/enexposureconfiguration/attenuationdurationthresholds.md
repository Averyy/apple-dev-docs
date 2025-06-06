# attenuationDurationThresholds

**Framework**: Exposure Notification  
**Kind**: property

The configurable signal-loss thresholds for calculating exposure risk.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var attenuationDurationThresholds: [NSNumber] { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.6 and later.

 This property is available in iOS 12.5, and in iOS 13.6 and later.

Signal attenuation and duration are measurable aspects of exposure risk. Set threshold values to configure the degree to which the signal loss between two devices for a specific duration signifies a potential exposure. Four categories are described in [`ENExposureConfiguration`](enexposureconfiguration.md): , , , and .

![Illustration showing the immediate attenuation threshold atop the immediate and near categories, the near attenuation threshold atop the near and medium categories, and the medium attenuation threshold atop the medium and other categories.](https://docs-assets.developer.apple.com/published/bb22dd39361dd13e579f70e52b2780b9/media-3699755%402x.png)

The following entries in the `attenuationDurationThresholds` array correspond to three thresholds for the four categories:

Attenuation values greater than `attenuationDurationThresholds[2]` accumulate into the “other” category.

## See Also

- [var immediateDurationWeight: Double](enexposureconfiguration/immediatedurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at immediate distance.
- [var mediumDurationWeight: Double](enexposureconfiguration/mediumdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at medium distance.
- [var nearDurationWeight: Double](enexposureconfiguration/neardurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at close distance.
- [var otherDurationWeight: Double](enexposureconfiguration/otherdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at a large distance.
- [var daysSinceLastExposureThreshold: Int](enexposureconfiguration/dayssincelastexposurethreshold.md)
  The number of days to consider when calculating the risk level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/attenuationdurationthresholds)*
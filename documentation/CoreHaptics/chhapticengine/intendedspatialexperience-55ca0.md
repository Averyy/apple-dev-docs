# intendedSpatialExperience

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property

The CHHapticEngine’s intended [`SpatialAudioExperience`](../../AudioToolbox/spatialaudioexperience.md).

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

## Discussion

Only useful for engines that have audio output.

If unspecified, the property value defaults to [`AutomaticSpatialAudio`](../../AudioToolbox/automaticspatialaudio.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/intendedspatialexperience-55ca0)*
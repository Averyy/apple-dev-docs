# intendedSpatialExperience

**Framework**: Core Haptics  
**Kind**: property

The CHHapticEngine’s intended [`SpatialAudioExperience`](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperience).

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

#### Discussion

Only useful for engines that have audio output.

If unspecified, the property value defaults to [`AutomaticSpatialAudio`](https://developer.apple.com/documentation/audiotoolbox/automaticspatialaudio).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/intendedspatialexperience-55ca0)*
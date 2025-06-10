# intendedSpatialExperience

**Framework**: Core Haptics  
**Kind**: property

The CHHapticEngine’s intended spatial experience.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

#### Discussion

Only useful for engines that have audio output. The default value of .automatic means the engine uses its AVAudioSession’s intended spatial experience. If the anchoring strategy is impossible (e.g. it uses a destroyed UIScene’s identifier), the engine follows a “front” anchoring strategy instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/intendedspatialexperience-55ca0)*
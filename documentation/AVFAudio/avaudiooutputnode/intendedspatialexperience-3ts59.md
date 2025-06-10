# intendedSpatialExperience

**Framework**: AVFAudio  
**Kind**: property

The AVAudioEngine output node’s intended spatial experience.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

#### Discussion

Only useful for engines that have an output node and are not configured in any manual rendering mode. The default value of .automatic means the engine uses its AVAudioSession’s intended spatial experience. See CASpatialAudioExperience for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiooutputnode/intendedspatialexperience-3ts59)*
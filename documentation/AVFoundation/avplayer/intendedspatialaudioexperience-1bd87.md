# intendedSpatialAudioExperience

**Framework**: AVFoundation  
**Kind**: property

The AVPlayer’s intended spatial audio experience.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
var intendedSpatialAudioExperience: any SpatialAudioExperience { get set }
```

#### Discussion

The default value of .automatic means the player uses its AVAudioSession’s intended spatial experience. See CASpatialAudioExperience for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/intendedspatialaudioexperience-1bd87)*
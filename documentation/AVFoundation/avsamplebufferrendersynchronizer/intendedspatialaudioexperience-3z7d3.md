# intendedSpatialAudioExperience

**Framework**: AVFoundation  
**Kind**: property

The synchronizer’s intended Spatial Audio experience.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var intendedSpatialAudioExperience: any SpatialAudioExperience { get set }
```

#### Discussion

The value applies to all [`AVSampleBufferAudioRenderer`](avsamplebufferaudiorenderer.md) objects within this synchronizer.

If unspecified, the property value defaults to [`CAAutomaticSpatialAudio`](https://developer.apple.com/documentation/AudioToolbox/CAAutomaticSpatialAudio).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3)*
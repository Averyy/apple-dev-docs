# intendedSpatialAudioExperience

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The intended spatial audio experience applied to all AVSampleBufferAudioRenderers within this synchronizer.

**Availability**:
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, copy) CASpatialAudioExperience * intendedSpatialAudioExperience;
```

## Discussion

The default value of CAAutomaticSpatialAudio means the renderers use their AVAudioSession’s intended spatial experience. If the anchoring strategy is impossible (e.g. it uses a destroyed UIScene’s identifier), the renderers follow a “front” anchoring strategy instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-2wthu)*
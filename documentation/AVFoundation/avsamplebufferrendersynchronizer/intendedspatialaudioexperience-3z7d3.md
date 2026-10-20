# intendedSpatialAudioExperience

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The synchronizer’s intended Spatial Audio experience.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var intendedSpatialAudioExperience: any SpatialAudioExperience { get set }
```

#### Discussion

The value applies to all [`AVSampleBufferAudioRenderer`](../avsamplebufferaudiorenderer.md) objects within this synchronizer.

If unspecified, the property value defaults to [`CAAutomaticSpatialAudio`](../../AudioToolbox/caautomaticspatialaudio.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3)*
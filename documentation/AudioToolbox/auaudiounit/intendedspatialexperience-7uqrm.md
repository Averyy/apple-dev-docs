# intendedSpatialExperience

**Framework**: Audio Toolbox  
**Kind**: property

The AUAudioUnit’s intended spatial audio experience.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

#### Discussion

This value is only useful for output audio units; otherwise it’s a no-op.

If unspecified, the property value defaults to [`AutomaticSpatialAudio`](automaticspatialaudio.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/intendedspatialexperience-7uqrm)*
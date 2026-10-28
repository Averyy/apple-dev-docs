# intendedSpatialExperience

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The AUAudioUnit’s intended spatial experience.

**Availability**:
- visionOS 26.0+

## Declaration

```objc
@property (copy, nonnull) CASpatialAudioExperience * intendedSpatialExperience;
```

## Discussion

Only useful for output AUAudioUnits - setting on a non-output AU is a no-op. The default value of CAAutomaticSpatialAudio means the output AUAudioUnit uses its AVAudioSession’s spatial experience. See CASpatialAudioExperience for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/intendedspatialexperience-1dvhd)*
# AudioServicesPlayAlertSound(_:spatialExperience:)

**Framework**: Audio Toolbox  
**Kind**: func

Play an alert sound with the provided spatial audio experience.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func AudioServicesPlayAlertSound(_ systemSoundID: SystemSoundID, spatialExperience: any SpatialAudioExperience) async
```

## Mentions

- [Anchoring sound to a window or volume](spatializing-sound-from-a-uiscene.md)

#### Discussion

The alert sound has this spatial experience for the duration of its playback and cannot change mid-playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesplayalertsound(_:spatialexperience:))*
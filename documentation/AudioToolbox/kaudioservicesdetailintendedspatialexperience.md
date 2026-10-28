# kAudioServicesDetailIntendedSpatialExperience

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- visionOS 26.0+

## Declaration

```c
extern CFStringRef const kAudioServicesDetailIntendedSpatialExperience;
```

## Discussion

Keys that are passed in a dictionary to AudioServicesPlaySystemSoundWithDetails

```
            Must be any non-nil CASpatialAudioExperience. The system sound
            will have this spatial experience for the duration of its
            playback and cannot change mid-playback.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioservicesdetailintendedspatialexperience)*
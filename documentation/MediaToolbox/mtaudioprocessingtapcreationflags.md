# MTAudioProcessingTapCreationFlags

**Framework**: Media Toolbox  
**Kind**: typealias

Flags to use when creating audio processing taps.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias MTAudioProcessingTapCreationFlags = UInt32
```

#### Discussion

You must set the pre or post flag, but not both.

## Topics

### Flags
- [var kMTAudioProcessingTapCreationFlag_PreEffects: MTAudioProcessingTapCreationFlags](kmtaudioprocessingtapcreationflag_preeffects.md)
  Signifies that the processing tap is inserted before any effects.
- [var kMTAudioProcessingTapCreationFlag_PostEffects: MTAudioProcessingTapCreationFlags](kmtaudioprocessingtapcreationflag_posteffects.md)
  Signifies that the processing tap is inserted before any effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcreationflags)*
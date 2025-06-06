# globalGain

**Framework**: AVFAudio  
**Kind**: property

The overall gain adjustment that the audio unit applies to the signal, in decibels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var globalGain: Float { get set }
```

#### Discussion

The default value is `0 db`. The valid range of values is `-96 db` to `24 db`.

## See Also

- [class AVAudioUnitEQFilterParameters](avaudiouniteqfilterparameters.md)
  An object that encapsulates the parameters that the equalizer uses.
- [var bands: [AVAudioUnitEQFilterParameters]](avaudiouniteq/bands.md)
  An array of equalizer filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteq/globalgain)*
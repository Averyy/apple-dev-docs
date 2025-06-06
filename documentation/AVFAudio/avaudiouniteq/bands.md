# bands

**Framework**: AVFAudio  
**Kind**: property

An array of equalizer filter parameters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bands: [AVAudioUnitEQFilterParameters] { get }
```

#### Discussion

The number of elements in the array is equal to the number of bands.

## See Also

- [class AVAudioUnitEQFilterParameters](avaudiouniteqfilterparameters.md)
  An object that encapsulates the parameters that the equalizer uses.
- [var globalGain: Float](avaudiouniteq/globalgain.md)
  The overall gain adjustment that the audio unit applies to the signal, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteq/bands)*
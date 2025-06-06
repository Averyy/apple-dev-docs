# preGain

**Framework**: AVFAudio  
**Kind**: property

The gain that the audio unit applies to the signal before distortion, in decibels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preGain: Float { get set }
```

#### Discussion

The default value is `-6 dB`. The valid range of values is `-80 dB` to `20 dB`.

## See Also

- [var wetDryMix: Float](avaudiounitdistortion/wetdrymix.md)
  The blend of the distorted and dry signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdistortion/pregain)*
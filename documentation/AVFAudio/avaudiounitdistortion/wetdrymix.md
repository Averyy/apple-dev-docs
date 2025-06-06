# wetDryMix

**Framework**: AVFAudio  
**Kind**: property

The blend of the distorted and dry signals.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var wetDryMix: Float { get set }
```

#### Discussion

You specify the blend as a percentage. The default value is `50%`. The valid range is `0%` through `100%`, where `0` represents all dry.

## See Also

- [var preGain: Float](avaudiounitdistortion/pregain.md)
  The gain that the audio unit applies to the signal before distortion, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdistortion/wetdrymix)*
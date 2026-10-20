# trailingFrames

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The number of trailing input frames, past the end input frame, the converter requires to perform a high-quality conversion.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var trailingFrames: AVAudioFrameCount
```

```c
AVAudioFrameCount trailingFrames;
```

## See Also

### Getting frame properties
- [var leadingFrames: AVAudioFrameCount](./leadingframes.md)
  The number of leading (previous) input frames the converter requires to perform a high-quality conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterprimeinfo/trailingframes)*
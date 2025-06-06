# nativeAudioFormat

**Framework**: Speech  
**Kind**: property

The preferred audio format for optimal speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var nativeAudioFormat: AVAudioFormat { get }
```

#### Discussion

Use the audio format in this property as a hint for optimal recording, but don’t depend on the value remaining unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/nativeaudioformat)*
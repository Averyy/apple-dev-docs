# AVAudioConverterInputBlock

**Framework**: AVFAudio  
**Kind**: typealias

A block to get input data for conversion, as necessary.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVAudioConverterInputBlock = (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterinputblock)*
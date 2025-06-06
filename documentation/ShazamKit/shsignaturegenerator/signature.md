# signature()

**Framework**: ShazamKit  
**Kind**: method

Converts the audio buffer into a signature.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func signature() -> SHSignature
```

#### Return Value

A signature that ShazamKit generates from the audio buffer.

## See Also

- [func append(AVAudioPCMBuffer, at: AVAudioTime?) throws](shsignaturegenerator/append(_:at:).md)
  Adds audio to the generator.
- [Generating a signature from an audio buffer](generating-a-signature-from-an-audio-buffer.md)
  Create a signature from an audio file or the microphone for a reference track in a custom catalog, or for matching tracks in a catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignaturegenerator/signature())*
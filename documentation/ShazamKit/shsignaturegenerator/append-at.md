# append(_:at:)

**Framework**: ShazamKit  
**Kind**: method

Adds audio to the generator.

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
func append(_ buffer: AVAudioPCMBuffer, at time: AVAudioTime?) throws
```

## Mentions

- [Generating a signature from an audio buffer](generating-a-signature-from-an-audio-buffer.md)

#### Discussion

Using noncontiguous audio may result in a lower-quality signature.

The audio must be PCM at one of these rates:

- `48000` hertz
- `44100` hertz
- `32000` hertz
- `16000` hertz

## Parameters

- `buffer`: The audio data to append to the signature generator.
- `time`: The time position of the start of the audio buffer in the full audio you use to generate the signature.

## See Also

- [func signature() -> SHSignature](shsignaturegenerator/signature.md)
  Converts the audio buffer into a signature.
- [Generating a signature from an audio buffer](generating-a-signature-from-an-audio-buffer.md)
  Create a signature from an audio file or the microphone for a reference track in a custom catalog, or for matching tracks in a catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignaturegenerator/append(_:at:))*
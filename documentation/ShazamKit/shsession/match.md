# match(_:)

**Framework**: ShazamKit  
**Kind**: method

Searches for the query signature in the reference signatures that the session catalog contains.

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
func match(_ signature: SHSignature)
```

## Parameters

- `signature`: The signature for searching the catalog of reference signatures.

## See Also

- [func matchStreamingBuffer(AVAudioPCMBuffer, at: AVAudioTime?)](shsession/matchstreamingbuffer(_:at:).md)
  Converts the audio in the buffer to a signature, and searches the reference signatures in the session catalog.
- [Matching audio using the built-in microphone](matching-audio-using-the-built-in-microphone.md)
  Use the audio stream from the microphone as the source for a ShazamKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/match(_:))*
# AudioReader.MicrophoneAsyncBuffers.Iterator

**Framework**: Create ML Components  
**Kind**: class

An async iterator of audio frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
final class Iterator
```

## Topics

### Getting the next element
- [func next() async throws -> TemporalFeature<AudioReader.MicrophoneAsyncBuffers.Feature>?](audioreader/microphoneasyncbuffers/iterator/next.md)
  Advances to the next element and returns it, or nil if no next element exists.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> AudioReader.MicrophoneAsyncBuffers.Iterator](audioreader/microphoneasyncbuffers/makeasynciterator.md)
  Constructs an iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/microphoneasyncbuffers/iterator)*
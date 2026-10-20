# AudioReader.MicrophoneAsyncBuffers.Iterator

**Framework**: Create ML Components  
**Kind**: class  
**Role**: Class

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
- [func next() async throws -> TemporalFeature<AudioReader.MicrophoneAsyncBuffers.Feature>?](./iterator/next%28%29.md)
  Advances to the next element and returns it, or nil if no next element exists.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> AudioReader.MicrophoneAsyncBuffers.Iterator](./makeasynciterator%28%29.md)
  Constructs an iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/microphoneasyncbuffers/iterator)*
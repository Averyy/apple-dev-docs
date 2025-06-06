# AudioReader.AsyncBuffers.Iterator

**Framework**: Create ML Components  
**Kind**: struct

An async iterator of audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Getting the next element
- [func next() async throws -> TemporalFeature<AVAudioPCMBuffer>?](audioreader/asyncbuffers/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [AudioReader.AsyncBuffers.Iterator.Element](audioreader/asyncbuffers/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](audioreader/asyncbuffers/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> AudioReader.AsyncBuffers.Iterator](audioreader/asyncbuffers/makeasynciterator.md)
  Constructs an iterator.
- [AudioReader.AsyncBuffers.AsyncIterator](audioreader/asyncbuffers/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AudioReader.AsyncBuffers.Feature](audioreader/asyncbuffers/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/asyncbuffers/iterator)*
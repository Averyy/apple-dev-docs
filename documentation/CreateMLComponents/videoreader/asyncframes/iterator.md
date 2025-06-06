# VideoReader.AsyncFrames.Iterator

**Framework**: Create ML Components  
**Kind**: struct

An async iterator of video frames.

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
- [func next() async throws -> TemporalFeature<CIImage>?](videoreader/asyncframes/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [VideoReader.AsyncFrames.Iterator.Element](videoreader/asyncframes/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](videoreader/asyncframes/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> VideoReader.AsyncFrames.Iterator](videoreader/asyncframes/makeasynciterator.md)
  Constructs an iterator.
- [VideoReader.AsyncFrames.AsyncIterator](videoreader/asyncframes/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [VideoReader.AsyncFrames.Feature](videoreader/asyncframes/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/asyncframes/iterator)*
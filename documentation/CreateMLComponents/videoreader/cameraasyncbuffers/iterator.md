# VideoReader.CameraAsyncBuffers.Iterator

**Framework**: Create ML Components  
**Kind**: class

An async iterator of video frames.

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
- [func next() async throws -> TemporalFeature<CIImage>?](videoreader/cameraasyncbuffers/iterator/next.md)
  Advances to the next element and returns it, or nil if no next element exists.
### Type Aliases
- [VideoReader.CameraAsyncBuffers.Iterator.Element](videoreader/cameraasyncbuffers/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](videoreader/cameraasyncbuffers/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> VideoReader.CameraAsyncBuffers.Iterator](videoreader/cameraasyncbuffers/makeasynciterator.md)
  Constructs an iterator.
- [VideoReader.CameraAsyncBuffers.AsyncIterator](videoreader/cameraasyncbuffers/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [VideoReader.CameraAsyncBuffers.Feature](videoreader/cameraasyncbuffers/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraasyncbuffers/iterator)*
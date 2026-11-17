# CameraFrameProvider.CameraFrameUpdates.Iterator

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An asynchronous iterator that produces camera frame elements on an asynchronous sequence.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Type methods
- [func next() async -> CameraFrameProvider.CameraFrameUpdates.Element?](./iterator/next%28%29.md)
  Asynchronously retrieve the next camera frame.
### Type aliases
- [CameraFrameProvider.CameraFrameUpdates.Element](./element.md)
  The type of element produced by this asynchronous sequence of camera frame structures.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Iterating over camera updates
- [func makeAsyncIterator() -> CameraFrameProvider.CameraFrameUpdates.Iterator](./makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces `CameraFrame` elements on this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates/iterator)*
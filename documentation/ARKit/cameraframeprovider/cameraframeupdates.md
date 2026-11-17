# CameraFrameProvider.CameraFrameUpdates

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A sequence of camera frames.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct CameraFrameUpdates
```

## Topics

### Iterating over camera updates
- [func makeAsyncIterator() -> CameraFrameProvider.CameraFrameUpdates.Iterator](./cameraframeupdates/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces `CameraFrame` elements on this asynchronous sequence.
- [CameraFrameProvider.CameraFrameUpdates.Iterator](./cameraframeupdates/iterator.md)
  An asynchronous iterator that produces camera frame elements on an asynchronous sequence.
### Type Aliases
- [CameraFrameProvider.CameraFrameUpdates.Element](./cameraframeupdates/element.md)
  The type of element produced by this asynchronous sequence of camera frame structures.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Getting camera frame updates
- [func cameraFrameUpdates(for: CameraVideoFormat) -> CameraFrameProvider.CameraFrameUpdates?](./cameraframeupdates%28for%29.md)
  Gets a sequence of camera frame updates for a given video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates)*
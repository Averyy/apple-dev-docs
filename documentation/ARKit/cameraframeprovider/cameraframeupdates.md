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

### Instance properties
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether this device supports the camera frame provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The authorization types you need to use the camera frame provider.
### Instance methods
- [func makeAsyncIterator() -> CameraFrameProvider.CameraFrameUpdates.Iterator](./cameraframeupdates/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces `CameraFrame` elements on this asynchronous sequence.
### Iterating over camera updates
- [CameraFrameProvider.CameraFrameUpdates.Iterator](./cameraframeupdates/iterator.md)
  An asynchronous iterator that produces camera frame elements on an asynchronous sequence.
### Type aliases
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
# CameraFrameProvider.CameraFrameUpdates

**Framework**: ARKit  
**Kind**: struct

A sequence of camera frames.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct CameraFrameUpdates
```

## Topics

### Instance properties
- [static var isSupported: Bool](cameraframeprovider/issupported.md)
  A Boolean value that indicates whether this device supports the camera frame provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](cameraframeprovider/requiredauthorizations.md)
  The authorization types you need to use the camera frame provider.
### Instance methods
- [func makeAsyncIterator() -> CameraFrameProvider.CameraFrameUpdates.Iterator](cameraframeprovider/cameraframeupdates/makeasynciterator.md)
### Iterating over camera updates
- [CameraFrameProvider.CameraFrameUpdates.Iterator](cameraframeprovider/cameraframeupdates/iterator.md)
  An asynchronous iterator that produces camera frame elements on an asynchronous sequence.
### Type aliases
- [CameraFrameProvider.CameraFrameUpdates.Element](cameraframeprovider/cameraframeupdates/element.md)
  The type of element produced by this asynchronous sequence of camera frame structures.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func cameraFrameUpdates(for: CameraVideoFormat) -> CameraFrameProvider.CameraFrameUpdates?](cameraframeprovider/cameraframeupdates(for:).md)
  Gets a sequence of camera frame updates for a given video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates)*
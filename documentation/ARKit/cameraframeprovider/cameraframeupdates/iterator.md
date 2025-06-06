# CameraFrameProvider.CameraFrameUpdates.Iterator

**Framework**: ARKit  
**Kind**: struct

An asynchronous iterator that produces camera frame elements on an asynchronous sequence.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Type methods
- [func next() async -> CameraFrameProvider.CameraFrameUpdates.Element?](cameraframeprovider/cameraframeupdates/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there’s no next element.
### Type aliases
- [CameraFrameProvider.CameraFrameUpdates.Element](cameraframeprovider/cameraframeupdates/element.md)
  The type of element produced by this asynchronous sequence of camera frame structures.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates/iterator)*
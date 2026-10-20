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
  Asynchronously advances to the next element and returns it, or ends the sequence if there’s no next element.
### Type aliases
- [CameraFrameProvider.CameraFrameUpdates.Element](./element.md)
  The type of element produced by this asynchronous sequence of camera frame structures.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates/iterator)*
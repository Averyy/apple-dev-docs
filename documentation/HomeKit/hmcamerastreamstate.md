# HMCameraStreamState

**Framework**: HomeKit  
**Kind**: enum

The states associated with a camera stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum HMCameraStreamState
```

## Topics

### Observing the streaming state
- [HMCameraStreamState.notStreaming](hmcamerastreamstate/notstreaming.md)
  The state when the camera stream is not active.
- [HMCameraStreamState.starting](hmcamerastreamstate/starting.md)
  The state when the camera stream start request is processing.
- [HMCameraStreamState.stopping](hmcamerastreamstate/stopping.md)
  The state when the camera stream is stopping.
- [HMCameraStreamState.streaming](hmcamerastreamstate/streaming.md)
  The state when the camera stream is currently in progress.
### Initializers
- [init?(rawValue: UInt)](hmcamerastreamstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func startStream()](hmcamerastreamcontrol/startstream.md)
  Starts the camera stream.
- [func stopStream()](hmcamerastreamcontrol/stopstream.md)
  Stops the camera stream.
- [var cameraStream: HMCameraStream?](hmcamerastreamcontrol/camerastream.md)
  The current camera stream.
- [class HMCameraStream](hmcamerastream.md)
  An object that represents a camera’s audiovisual stream.
- [var streamState: HMCameraStreamState](hmcamerastreamcontrol/streamstate.md)
  The current state of the camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamstate)*
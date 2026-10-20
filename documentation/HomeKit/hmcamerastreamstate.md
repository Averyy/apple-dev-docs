# HMCameraStreamState

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HMCameraStreamState : NSUInteger;
```

## Topics

### Observing the streaming state
- [HMCameraStreamState.notStreaming](./hmcamerastreamstate/notstreaming.md)
  The state when the camera stream is not active.
- [HMCameraStreamState.starting](./hmcamerastreamstate/starting.md)
  The state when the camera stream start request is processing.
- [HMCameraStreamState.stopping](./hmcamerastreamstate/stopping.md)
  The state when the camera stream is stopping.
- [HMCameraStreamState.streaming](./hmcamerastreamstate/streaming.md)
  The state when the camera stream is currently in progress.
### Initializers
- [init?(rawValue: UInt)](./hmcamerastreamstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling the stream
- [func startStream()](./hmcamerastreamcontrol/startstream%28%29.md)
  Starts the camera stream.
- [func stopStream()](./hmcamerastreamcontrol/stopstream%28%29.md)
  Stops the camera stream.
- [var cameraStream: HMCameraStream?](./hmcamerastreamcontrol/camerastream.md)
  The current camera stream.
- [class HMCameraStream](./hmcamerastream.md)
  An object that represents a camera’s audiovisual stream.
- [var streamState: HMCameraStreamState](./hmcamerastreamcontrol/streamstate.md)
  The current state of the camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamstate)*
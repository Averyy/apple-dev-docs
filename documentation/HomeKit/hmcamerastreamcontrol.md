# HMCameraStreamControl

**Framework**: HomeKit  
**Kind**: class

An object that can start and stop the camera stream and contains the view into which the stream is rendered.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraStreamControl
```

## Topics

### Controlling the stream
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
- [enum HMCameraStreamState](hmcamerastreamstate.md)
  The states associated with a camera stream.
### Observing stream activity
- [var delegate: (any HMCameraStreamControlDelegate)?](hmcamerastreamcontrol/delegate.md)
  Delegate that receives updates as the camera stream changes.
- [protocol HMCameraStreamControlDelegate](hmcamerastreamcontroldelegate.md)
  A protocol that gives the delegate updates on the camera stream.
### Initializers
- [init()](hmcamerastreamcontrol/init.md)

## Relationships

### Inherits From
- [HMCameraControl](hmcameracontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var streamControl: HMCameraStreamControl?](hmcameraprofile/streamcontrol.md)
  Controls the camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol)*
# streamState

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The current state of the camera stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var streamState: HMCameraStreamState { get }
```

```objc
@property (nonatomic, assign, readonly) HMCameraStreamState streamState;
```

## See Also

### Controlling the stream
- [func startStream()](./startstream%28%29.md)
  Starts the camera stream.
- [func stopStream()](./stopstream%28%29.md)
  Stops the camera stream.
- [var cameraStream: HMCameraStream?](./camerastream.md)
  The current camera stream.
- [class HMCameraStream](../hmcamerastream.md)
  An object that represents a camera’s audiovisual stream.
- [enum HMCameraStreamState](../hmcamerastreamstate.md)
  The states associated with a camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/streamstate)*
# startStream()

**Framework**: HomeKit  
**Kind**: method

Starts the camera stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func startStream()
```

#### Discussion

When streaming has successfully started, the [`cameraStream`](hmcamerastreamcontrol/camerastream.md) property is updated with the new stream.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/startstream())*
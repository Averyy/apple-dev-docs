# startStream()

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) startStream;
```

## Discussion

When streaming has successfully started, the [`cameraStream`](./camerastream.md) property is updated with the new stream.

## See Also

### Controlling the stream
- [func stopStream()](./stopstream%28%29.md)
  Stops the camera stream.
- [var cameraStream: HMCameraStream?](./camerastream.md)
  The current camera stream.
- [class HMCameraStream](../hmcamerastream.md)
  An object that represents a camera’s audiovisual stream.
- [var streamState: HMCameraStreamState](./streamstate.md)
  The current state of the camera stream.
- [enum HMCameraStreamState](../hmcamerastreamstate.md)
  The states associated with a camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/startstream())*
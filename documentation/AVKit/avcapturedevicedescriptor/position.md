# position

**Framework**: AVKit  
**Kind**: property

The physical position of the camera on the device.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var position: AVCaptureDevice.Position { get }
```

#### Discussion

This value matches the [`position`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.property) of the camera it describes. Position describes the hardware, not the direction the camera faces in relation to your view.

## See Also

- [var deviceType: AVCaptureDevice.DeviceType](avcapturedevicedescriptor/devicetype.md)
  The kind of camera, such as a wide-angle or telephoto camera.
- [var mediaTypes: Set<AVMediaType>](avcapturedevicedescriptor/mediatypes.md)
  The kinds of media the camera captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/position)*
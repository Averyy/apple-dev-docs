# position

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The physical position of the camera on the device.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var position: AVCaptureDevice.Position { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDevicePosition position;
```

## Discussion

This value matches the [`position`](../../AVFoundation/avcapturedevice/position-swift.property.md) of the camera it describes. Position describes the hardware, not the direction the camera faces in relation to your view.

## See Also

### Inspecting the device’s characteristics
- [var deviceType: AVCaptureDevice.DeviceType](./devicetype.md)
  The kind of camera, such as a wide-angle or telephoto camera.
- [var mediaTypes: Set<AVMediaType>](./mediatypes.md)
  The kinds of media the camera captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/position)*
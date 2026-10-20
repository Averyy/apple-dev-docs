# deviceType

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The kind of camera, such as a wide-angle or telephoto camera.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var deviceType: AVCaptureDevice.DeviceType { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDeviceType deviceType;
```

#### Discussion

This value matches the https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype of the camera it describes.

## See Also

### Inspecting the device’s characteristics
- [var mediaTypes: Set<AVMediaType>](./mediatypes.md)
  The kinds of media the camera captures.
- [var position: AVCaptureDevice.Position](./position.md)
  The physical position of the camera on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/devicetype)*
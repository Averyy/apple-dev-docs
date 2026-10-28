# sourceDeviceType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The device type of the source camera that provides data to the port.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var sourceDeviceType: AVCaptureDevice.DeviceType? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVCaptureDeviceType sourceDeviceType;
```

## Discussion

All ports contained in an input’s [`ports`](../ports.md) property have the same source device type, which each equal to the [`deviceType`](../../avcapturedevice/devicetype-swift.property.md) property of the input’s device.

When working with virtual devices such as the [`builtInDualCamera`](../../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) in an [`AVCaptureMultiCamSession`](../../avcapturemulticamsession.md), it’s possible to stream media from the virtual device’s constituent device streams by discovering and connecting hidden ports. In the case of the [`builtInDualCamera`](../../avcapturedevice/devicetype-swift.struct/builtindualcamera.md), its constituent devices are the wide-angle and telephoto cameras.

By calling [`ports(for:sourceDeviceType:sourceDevicePosition:)`](../../avcapturedeviceinput/ports%28for,sourcedevicetype,sourcedeviceposition%29.md):, you may discover ports originating from one or more of the virtual device’s constituent devices and then make connections using those ports. Constituent device ports are never present in their owning virtual device input’s ports array.

## See Also

### Inspecting an input port
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](./formatdescription.md)
  A description of the port format.
- [var sourceDevicePosition: AVCaptureDevice.Position](./sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](./clock.md)
  An object that represents the capture device’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/sourcedevicetype)*
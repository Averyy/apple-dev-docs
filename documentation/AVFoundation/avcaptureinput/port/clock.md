# clock

**Framework**: AVFoundation  
**Kind**: property

An object that represents the capture device’s clock.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.9+
- tvOS 17.0+

## Declaration

```swift
var clock: CMClock? { get }
```

#### Discussion

The value of this property is readonly and may not reflect the actual clock in the capture device.

## See Also

- [var isEnabled: Bool](avcaptureinput/port/isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](avcaptureinput/port/mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](avcaptureinput/port/formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcaptureinput/port/sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](avcaptureinput/port/sourcedeviceposition.md)
  The position of the source device providing input through this port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/clock)*
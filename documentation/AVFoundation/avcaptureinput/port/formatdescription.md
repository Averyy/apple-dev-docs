# formatDescription

**Framework**: AVFoundation  
**Kind**: property

A description of the port format.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var formatDescription: CMFormatDescription? { get }
```

#### Discussion

A format description object describes the format of the media the port currently provides. To observe changes to a port’s format, observe notifications of type [`formatDescriptionDidChangeNotification`](avcaptureinput/port/formatdescriptiondidchangenotification.md).

## See Also

- [var isEnabled: Bool](avcaptureinput/port/isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](avcaptureinput/port/mediatype.md)
  The media type of the port.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcaptureinput/port/sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](avcaptureinput/port/sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](avcaptureinput/port/clock.md)
  An object that represents the capture device’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/formatdescription)*
# formatDescription

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) CMFormatDescriptionRef formatDescription;
```

## Discussion

A format description object describes the format of the media the port currently provides. To observe changes to a port’s format, observe notifications of type [`formatDescriptionDidChangeNotification`](./formatdescriptiondidchangenotification.md).

## See Also

### Inspecting an input port
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the port.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](./sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](./clock.md)
  An object that represents the capture device’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/formatdescription)*
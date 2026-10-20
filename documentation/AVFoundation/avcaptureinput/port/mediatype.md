# mediaType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The media type of the port.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var mediaType: AVMediaType { get }
```

```objc
@property (nonatomic, readonly) AVMediaType mediaType;
```

## See Also

### Inspecting an input port
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var formatDescription: CMFormatDescription?](./formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](./sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](./clock.md)
  An object that represents the capture device’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/mediatype)*
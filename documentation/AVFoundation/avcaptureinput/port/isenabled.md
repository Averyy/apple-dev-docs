# isEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the port is in an enabled state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

Ports are in an enabled state by default. If you want to capture only a subset of the media streams provided by a capture input, use this property to selectively disable streams.

## See Also

### Inspecting an input port
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](./formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](./sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](./clock.md)
  An object that represents the capture device’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/isenabled)*
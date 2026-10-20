# clock

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) CMClockRef clock;
```

#### Discussion

The value of this property is readonly and may not reflect the actual clock in the capture device.

## See Also

### Inspecting an input port
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](./formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](./sourcedeviceposition.md)
  The position of the source device providing input through this port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/clock)*
# device

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A capture device associated with this input.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var device: AVCaptureDevice { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDevice * device;
```

## See Also

### Accessing the device
- [func ports(for: AVMediaType?, sourceDeviceType: AVCaptureDevice.DeviceType?, sourceDevicePosition: AVCaptureDevice.Position) -> [AVCaptureInput.Port]](./ports%28for,sourcedevicetype,sourcedeviceposition%29.md)
  Retrieves a virtual device’s constituent device ports for use in a multi-camera session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/device)*
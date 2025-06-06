# exposureMode

**Framework**: AVFoundation  
**Kind**: property

The exposure mode for the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var exposureMode: AVCaptureDevice.ExposureMode { get set }
```

#### Discussion

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

- [func isExposureModeSupported(AVCaptureDevice.ExposureMode) -> Bool](avcapturedevice/isexposuremodesupported(_:).md)
  Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [AVCaptureDevice.ExposureMode](avcapturedevice/exposuremode-swift.enum.md)
  Constants that specify the exposure mode of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.property)*
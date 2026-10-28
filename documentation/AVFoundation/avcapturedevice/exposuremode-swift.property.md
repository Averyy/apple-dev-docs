# exposureMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) AVCaptureExposureMode exposureMode;
```

## Discussion

Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Managing the exposure mode
- [func isExposureModeSupported(AVCaptureDevice.ExposureMode) -> Bool](./isexposuremodesupported%28_%29.md)
  Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [AVCaptureDevice.ExposureMode](./exposuremode-swift.enum.md)
  Constants that specify the exposure mode of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.property)*
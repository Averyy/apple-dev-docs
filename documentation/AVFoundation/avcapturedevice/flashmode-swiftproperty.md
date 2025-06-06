# flashMode

**Framework**: AVFoundation  
**Kind**: property

The device’s current flash mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
var flashMode: AVCaptureDevice.FlashMode { get set }
```

#### Discussion

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

- [var hasFlash: Bool](avcapturedevice/hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](avcapturedevice/isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](avcapturedevice/isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](avcapturedevice/isflashmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode-swift.property)*
# flashMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The device’s current flash mode.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+

> **Deprecated**: Use [`flashMode`](../avcapturephotosettings/flashmode.md) on [`AVCapturePhotoSettings`](../avcapturephotosettings.md) instead.

## Declaration

```swift
var flashMode: AVCaptureDevice.FlashMode { get set }
```

```objc
@property (nonatomic) AVCaptureFlashMode flashMode;
```

## Discussion

Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Configuring flash settings
- [var hasFlash: Bool](./hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](./isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](./isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](./isflashmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](./flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode-swift.property)*
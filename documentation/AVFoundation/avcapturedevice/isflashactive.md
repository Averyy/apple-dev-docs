# isFlashActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the flash is currently active.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`isFlashScene`](../avcapturephotooutput/isflashscene.md) on [`AVCapturePhotoOutput`](../avcapturephotooutput.md) instead.

## Declaration

```swift
var isFlashActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFlashActive) BOOL flashActive;
```

#### Discussion

When the flash is active, it flashes when capturing a photo.

This property is key-value observable.

## See Also

### Configuring flash settings
- [var hasFlash: Bool](./hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](./isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var flashMode: AVCaptureDevice.FlashMode](./flashmode-swift.property.md)
  The device’s current flash mode.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](./isflashmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](./flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashactive)*
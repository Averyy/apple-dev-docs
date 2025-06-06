# isFlashActive

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the flash is currently active.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isFlashActive: Bool { get }
```

#### Discussion

When the flash is active, it flashes when capturing a photo.

This property is key-value observable.

## See Also

- [var hasFlash: Bool](avcapturedevice/hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](avcapturedevice/isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var flashMode: AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.property.md)
  The device’s current flash mode.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](avcapturedevice/isflashmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashactive)*
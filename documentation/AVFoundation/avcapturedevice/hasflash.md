# hasFlash

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture device has a flash.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var hasFlash: Bool { get }
```

#### Discussion

This property is key-value observable.

## See Also

- [var isFlashAvailable: Bool](avcapturedevice/isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](avcapturedevice/isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [var flashMode: AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.property.md)
  The device’s current flash mode.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](avcapturedevice/isflashmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/hasflash)*
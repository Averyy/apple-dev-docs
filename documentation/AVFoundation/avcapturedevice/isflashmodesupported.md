# isFlashModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether the device supports the given flash mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func isFlashModeSupported(_ flashMode: AVCaptureDevice.FlashMode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports the flash mode; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `flashMode`: A flash mode to test if the device supports.

## See Also

- [var hasFlash: Bool](avcapturedevice/hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](avcapturedevice/isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](avcapturedevice/isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [var flashMode: AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.property.md)
  The device’s current flash mode.
- [AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashmodesupported(_:))*
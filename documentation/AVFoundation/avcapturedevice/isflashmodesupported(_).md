# isFlashModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the device supports the given flash mode.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+

> **Deprecated**: Use [`supportedFlashModes`](../avcapturephotooutput/supportedflashmodes-1n6nm.md) on [`AVCapturePhotoOutput`](../avcapturephotooutput.md) instead.

## Declaration

```swift
func isFlashModeSupported(_ flashMode: AVCaptureDevice.FlashMode) -> Bool
```

```objc
- (BOOL) isFlashModeSupported:(AVCaptureFlashMode) flashMode;
```

#### Return Value

[`true`](../../Swift/true.md) if the device supports the flash mode; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `flashMode`: A flash mode to test if the device supports.

## See Also

### Configuring flash settings
- [var hasFlash: Bool](./hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](./isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](./isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [var flashMode: AVCaptureDevice.FlashMode](./flashmode-swift.property.md)
  The device’s current flash mode.
- [AVCaptureDevice.FlashMode](./flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashmodesupported(_:))*
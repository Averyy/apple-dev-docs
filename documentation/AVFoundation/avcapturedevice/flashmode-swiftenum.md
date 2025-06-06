# AVCaptureDevice.FlashMode

**Framework**: AVFoundation  
**Kind**: enum

Constants that specify the flash modes of a capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
enum FlashMode
```

## Topics

### Flash Modes
- [AVCaptureDevice.FlashMode.off](avcapturedevice/flashmode-swift.enum/off.md)
  A mode that indicates the flash is off.
- [AVCaptureDevice.FlashMode.on](avcapturedevice/flashmode-swift.enum/on.md)
  A mode that indicates the flash is on.
- [AVCaptureDevice.FlashMode.auto](avcapturedevice/flashmode-swift.enum/auto.md)
  A mode that indicates the device continuously monitors light levels and uses the flash when necessary.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/flashmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var hasFlash: Bool](avcapturedevice/hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](avcapturedevice/isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](avcapturedevice/isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [var flashMode: AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.property.md)
  The device’s current flash mode.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](avcapturedevice/isflashmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode-swift.enum)*
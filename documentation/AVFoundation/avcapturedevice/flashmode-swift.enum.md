# AVCaptureDevice.FlashMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureFlashMode : NSInteger;
```

## Topics

### Flash modes
- [AVCaptureDevice.FlashMode.off](./flashmode-swift.enum/off.md)
  A mode that indicates the flash is off.
- [AVCaptureDevice.FlashMode.on](./flashmode-swift.enum/on.md)
  A mode that indicates the flash is on.
- [AVCaptureDevice.FlashMode.auto](./flashmode-swift.enum/auto.md)
  A mode that indicates the device continuously monitors light levels and uses the flash when necessary.
### Initializers
- [init?(rawValue: Int)](./flashmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](./isflashmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode-swift.enum)*
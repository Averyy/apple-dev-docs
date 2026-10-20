# isFlashAvailable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the flash is currently available for use.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var isFlashAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFlashAvailable) BOOL flashAvailable;
```

#### Discussion

The flash may become unavailable if, for example, the device overheats and needs to cool off.

This property is key-value observable.

## See Also

### Configuring flash settings
- [var hasFlash: Bool](./hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashActive: Bool](./isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [var flashMode: AVCaptureDevice.FlashMode](./flashmode-swift.property.md)
  The device’s current flash mode.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](./isflashmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](./flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashavailable)*
# AVCaptureDevice.WhiteBalanceMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants to specify the white balance mode of a capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
enum WhiteBalanceMode
```

```c
enum AVCaptureWhiteBalanceMode : NSInteger;
```

## Topics

### White balance modes
- [AVCaptureDevice.WhiteBalanceMode.locked](./whitebalancemode-swift.enum/locked.md)
  A mode that locks the white balance state.
- [AVCaptureDevice.WhiteBalanceMode.autoWhiteBalance](./whitebalancemode-swift.enum/autowhitebalance.md)
  A mode that automatically manages white balance.
- [AVCaptureDevice.WhiteBalanceMode.continuousAutoWhiteBalance](./whitebalancemode-swift.enum/continuousautowhitebalance.md)
  A mode that continuously monitors white balance and adjusts when necessary.
### Initializers
- [init?(rawValue: Int)](./whitebalancemode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring automatic white balance
- [func isWhiteBalanceModeSupported(AVCaptureDevice.WhiteBalanceMode) -> Bool](./iswhitebalancemodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [var whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode](./whitebalancemode-swift.property.md)
  The current white balance mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.enum)*
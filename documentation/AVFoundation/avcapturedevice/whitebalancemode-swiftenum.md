# AVCaptureDevice.WhiteBalanceMode

**Framework**: AVFoundation  
**Kind**: enum

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

## Topics

### White Balance Modes
- [AVCaptureDevice.WhiteBalanceMode.locked](avcapturedevice/whitebalancemode-swift.enum/locked.md)
  A mode that locks the white balance state.
- [AVCaptureDevice.WhiteBalanceMode.autoWhiteBalance](avcapturedevice/whitebalancemode-swift.enum/autowhitebalance.md)
  A mode that automatically manages white balance.
- [AVCaptureDevice.WhiteBalanceMode.continuousAutoWhiteBalance](avcapturedevice/whitebalancemode-swift.enum/continuousautowhitebalance.md)
  A mode that continuously monitors white balance and adjusts when necessary.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/whitebalancemode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func isWhiteBalanceModeSupported(AVCaptureDevice.WhiteBalanceMode) -> Bool](avcapturedevice/iswhitebalancemodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [var whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode](avcapturedevice/whitebalancemode-swift.property.md)
  The current white balance mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.enum)*
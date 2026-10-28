# isWhiteBalanceModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the device supports the specified white balance mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func isWhiteBalanceModeSupported(_ whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode) -> Bool
```

```objc
- (BOOL) isWhiteBalanceModeSupported:(AVCaptureWhiteBalanceMode) whiteBalanceMode;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports the white balance mode; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `whiteBalanceMode`: A white balance mode to use.

## See Also

### Configuring automatic white balance
- [var whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode](./whitebalancemode-swift.property.md)
  The current white balance mode.
- [AVCaptureDevice.WhiteBalanceMode](./whitebalancemode-swift.enum.md)
  Constants to specify the white balance mode of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iswhitebalancemodesupported(_:))*
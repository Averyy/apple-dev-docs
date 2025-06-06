# whiteBalanceMode

**Framework**: AVFoundation  
**Kind**: property

The current white balance mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode { get set }
```

#### Discussion

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

- [func isWhiteBalanceModeSupported(AVCaptureDevice.WhiteBalanceMode) -> Bool](avcapturedevice/iswhitebalancemodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [AVCaptureDevice.WhiteBalanceMode](avcapturedevice/whitebalancemode-swift.enum.md)
  Constants to specify the white balance mode of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.property)*
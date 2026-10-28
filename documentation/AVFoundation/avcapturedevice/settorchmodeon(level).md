# setTorchModeOn(level:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the illumination level when in torch mode.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func setTorchModeOn(level torchLevel: Float) throws
```

```objc
- (BOOL) setTorchModeOnWithLevel:(float) torchLevel error:(NSError **) outError;
```

## Discussion

This method sets the torch mode to [`AVCaptureDevice.TorchMode.on`](./torchmode-swift.enum/on.md) and sets the level to the specified value. If the device doesn’t support this mode or if you specify a value for `torchLevel` that’s outside the accepted range, this method raises an exception. If the torch value is within the accepted range but greater than the currently supported maximum—perhaps because the device is overheating—this method returns [`false`](../../Swift/false.md).

Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, calling this method raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

## Parameters

- `torchLevel`: The new torch mode level. This value must be a floating-point number between `0.0` and `1.0`. To set the torch mode level to the currently available maximum, specify the constant [`maxAvailableTorchLevel`](./maxavailabletorchlevel.md) for this parameter.

## See Also

### Configuring torch settings
- [var hasTorch: Bool](./hastorch.md)
  A Boolean value that specifies whether the capture device has a torch.
- [var isTorchAvailable: Bool](./istorchavailable.md)
  A Boolean value that indicates whether the torch is currently available for use.
- [var isTorchActive: Bool](./istorchactive.md)
  A Boolean value that indicates whether the device’s torch is currently active.
- [var torchLevel: Float](./torchlevel.md)
  The current torch brightness level.
- [var torchMode: AVCaptureDevice.TorchMode](./torchmode-swift.property.md)
  The current torch mode.
- [AVCaptureDevice.TorchMode](./torchmode-swift.enum.md)
  Constants to specify the capture device’s torch mode.
- [func isTorchModeSupported(AVCaptureDevice.TorchMode) -> Bool](./istorchmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [class let maxAvailableTorchLevel: Float](./maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/settorchmodeon(level:))*
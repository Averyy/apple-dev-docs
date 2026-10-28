# torchMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current torch mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var torchMode: AVCaptureDevice.TorchMode { get set }
```

```objc
@property (nonatomic) AVCaptureTorchMode torchMode;
```

## Discussion

Setting the value of this property also sets the torch level to its maximum current value.

Before setting the value of this property, call the [`isTorchModeSupported(_:)`](./istorchmodesupported%28_%29.md) method to make sure the device supports the desired mode. Setting the device to an unsupported torch mode results in the raising of an exception. For a list of possible values for this property, see [`AVCaptureDevice.TorchMode`](./torchmode-swift.enum.md).

Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

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
- [AVCaptureDevice.TorchMode](./torchmode-swift.enum.md)
  Constants to specify the capture device’s torch mode.
- [func isTorchModeSupported(AVCaptureDevice.TorchMode) -> Bool](./istorchmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [func setTorchModeOn(level: Float) throws](./settorchmodeon%28level%29.md)
  Sets the illumination level when in torch mode.
- [class let maxAvailableTorchLevel: Float](./maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode-swift.property)*
# torchLevel

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current torch brightness level.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var torchLevel: Float { get }
```

```objc
@property (nonatomic, readonly) float torchLevel;
```

## Discussion

The value of this property is a floating-point number whose value is in the range 0.0 to 1.0. A torch level of 0.0 indicates that the torch is off. A torch level of 1.0 represents the theoretical maximum value, although the actual maximum value may be lower if the device is currently overheated.

This property is key-value observable.

## See Also

### Configuring torch settings
- [var hasTorch: Bool](./hastorch.md)
  A Boolean value that specifies whether the capture device has a torch.
- [var isTorchAvailable: Bool](./istorchavailable.md)
  A Boolean value that indicates whether the torch is currently available for use.
- [var isTorchActive: Bool](./istorchactive.md)
  A Boolean value that indicates whether the device’s torch is currently active.
- [var torchMode: AVCaptureDevice.TorchMode](./torchmode-swift.property.md)
  The current torch mode.
- [AVCaptureDevice.TorchMode](./torchmode-swift.enum.md)
  Constants to specify the capture device’s torch mode.
- [func isTorchModeSupported(AVCaptureDevice.TorchMode) -> Bool](./istorchmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [func setTorchModeOn(level: Float) throws](./settorchmodeon%28level%29.md)
  Sets the illumination level when in torch mode.
- [class let maxAvailableTorchLevel: Float](./maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchlevel)*
# hasTorch

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the capture device has a torch.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var hasTorch: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasTorch;
```

## Discussion

A torch is a light source, such as an LED flash, that’s available on the device and used for illuminating captured content or providing general illumination. This property reflects whether the current device has such illumination hardware built-in.

Even if the device has a torch, that torch might not be available for use, so check the value of the [`isTorchAvailable`](./istorchavailable.md) property before using it.

This property is key-value observable.

## See Also

### Configuring torch settings
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
- [func setTorchModeOn(level: Float) throws](./settorchmodeon%28level%29.md)
  Sets the illumination level when in torch mode.
- [class let maxAvailableTorchLevel: Float](./maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/hastorch)*
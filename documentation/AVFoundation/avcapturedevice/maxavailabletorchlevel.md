# maxAvailableTorchLevel

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A constant that indicates to set the torch to its maximum level.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
class let maxAvailableTorchLevel: Float
```

```c
extern const float AVCaptureMaxAvailableTorchLevel;
```

## Discussion

Pass this value to the [`setTorchModeOn(level:)`](./settorchmodeon%28level%29.md) method to set the torch to the maximum level currently available. Under thermal duress, the maximum available torch level may be less than 1.0.

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
- [func setTorchModeOn(level: Float) throws](./settorchmodeon%28level%29.md)
  Sets the illumination level when in torch mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxavailabletorchlevel)*
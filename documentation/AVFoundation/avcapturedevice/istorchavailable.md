# isTorchAvailable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the torch is currently available for use.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var isTorchAvailable: Bool { get }
```

#### Discussion

The torch may become unavailable if, for example, the device overheats and needs to cool off.

This property is key-value observable.

## See Also

- [var hasTorch: Bool](avcapturedevice/hastorch.md)
  A Boolean value that specifies whether the capture device has a torch.
- [var isTorchActive: Bool](avcapturedevice/istorchactive.md)
  A Boolean value that indicates whether the device’s torch is currently active.
- [var torchLevel: Float](avcapturedevice/torchlevel.md)
  The current torch brightness level.
- [var torchMode: AVCaptureDevice.TorchMode](avcapturedevice/torchmode-swift.property.md)
  The current torch mode.
- [AVCaptureDevice.TorchMode](avcapturedevice/torchmode-swift.enum.md)
  Constants to specify the capture device’s torch mode.
- [func isTorchModeSupported(AVCaptureDevice.TorchMode) -> Bool](avcapturedevice/istorchmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [func setTorchModeOn(level: Float) throws](avcapturedevice/settorchmodeon(level:).md)
  Sets the illumination level when in torch mode.
- [class let maxAvailableTorchLevel: Float](avcapturedevice/maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/istorchavailable)*
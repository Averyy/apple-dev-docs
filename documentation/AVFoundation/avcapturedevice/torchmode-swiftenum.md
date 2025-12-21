# AVCaptureDevice.TorchMode

**Framework**: AVFoundation  
**Kind**: enum

Constants to specify the capture device’s torch mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
enum TorchMode
```

## Topics

### Torch modes
- [AVCaptureDevice.TorchMode.off](avcapturedevice/torchmode-swift.enum/off.md)
  The capture device torch is always off.
- [AVCaptureDevice.TorchMode.on](avcapturedevice/torchmode-swift.enum/on.md)
  The capture device torch is always on.
- [AVCaptureDevice.TorchMode.auto](avcapturedevice/torchmode-swift.enum/auto.md)
  The capture device continuously monitors light levels and uses the torch when necessary.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/torchmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var hasTorch: Bool](avcapturedevice/hastorch.md)
  A Boolean value that specifies whether the capture device has a torch.
- [var isTorchAvailable: Bool](avcapturedevice/istorchavailable.md)
  A Boolean value that indicates whether the torch is currently available for use.
- [var isTorchActive: Bool](avcapturedevice/istorchactive.md)
  A Boolean value that indicates whether the device’s torch is currently active.
- [var torchLevel: Float](avcapturedevice/torchlevel.md)
  The current torch brightness level.
- [var torchMode: AVCaptureDevice.TorchMode](avcapturedevice/torchmode-swift.property.md)
  The current torch mode.
- [func isTorchModeSupported(AVCaptureDevice.TorchMode) -> Bool](avcapturedevice/istorchmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [func setTorchModeOn(level: Float) throws](avcapturedevice/settorchmodeon(level:).md)
  Sets the illumination level when in torch mode.
- [class let maxAvailableTorchLevel: Float](avcapturedevice/maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode-swift.enum)*
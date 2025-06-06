# AVCaptureDevice.Format.AutoFocusSystem

**Framework**: AVFoundation  
**Kind**: enum

An enumeration of auto focus systems.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
enum AutoFocusSystem
```

## Topics

### Systems
- [AVCaptureDevice.Format.AutoFocusSystem.none](avcapturedevice/format/autofocussystem-swift.enum/none.md)
  Autofocus isn’t available.
- [AVCaptureDevice.Format.AutoFocusSystem.contrastDetection](avcapturedevice/format/autofocussystem-swift.enum/contrastdetection.md)
  A slower autofocus system based on differences in contrast.
- [AVCaptureDevice.Format.AutoFocusSystem.phaseDetection](avcapturedevice/format/autofocussystem-swift.enum/phasedetection.md)
  A faster autofoscus system based on differences in light phase.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/format/autofocussystem-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var autoFocusSystem: AVCaptureDevice.Format.AutoFocusSystem](avcapturedevice/format/autofocussystem-swift.property.md)
  The auto focus system the format uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum)*
# AVCaptureDevice.Format.AutoFocusSystem

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureAutoFocusSystem : NSInteger;
```

## Topics

### Systems
- [AVCaptureDevice.Format.AutoFocusSystem.none](./autofocussystem-swift.enum/none.md)
  Autofocus isn’t available.
- [AVCaptureDevice.Format.AutoFocusSystem.contrastDetection](./autofocussystem-swift.enum/contrastdetection.md)
  A slower autofocus system based on differences in contrast.
- [AVCaptureDevice.Format.AutoFocusSystem.phaseDetection](./autofocussystem-swift.enum/phasedetection.md)
  A faster autofoscus system based on differences in light phase.
### Initializers
- [init?(rawValue: Int)](./autofocussystem-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Determining the auto focus system
- [var autoFocusSystem: AVCaptureDevice.Format.AutoFocusSystem](./autofocussystem-swift.property.md)
  The auto focus system the format uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum)*
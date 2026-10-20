# AVCaptureDevice.SystemPressureState.Level

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines system pressure state levels.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Level
```

```c
typedef NSString * AVCaptureSystemPressureLevel;
```

## Topics

### System pressure levels
- [static let nominal: AVCaptureDevice.SystemPressureState.Level](./level-swift.struct/nominal.md)
  A level that indicates the system pressure is normal and not under pressure.
- [static let fair: AVCaptureDevice.SystemPressureState.Level](./level-swift.struct/fair.md)
  A level that indicates that system pressure is slightly elevated.
- [static let serious: AVCaptureDevice.SystemPressureState.Level](./level-swift.struct/serious.md)
  A level that indicates that system pressure is highly elevated.
- [static let critical: AVCaptureDevice.SystemPressureState.Level](./level-swift.struct/critical.md)
  System pressure is critically elevated.
- [static let shutdown: AVCaptureDevice.SystemPressureState.Level](./level-swift.struct/shutdown.md)
  System pressure is beyond critical, so the capture system has shut down.
### Initializers
- [init(rawValue: String)](./level-swift.struct/init%28rawvalue%29.md)
  Creates a system pressure level from its raw string value.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Overall level
- [var level: AVCaptureDevice.SystemPressureState.Level](./level-swift.property.md)
  The overall level of performance constraints on the capture system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct)*
# nominal

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A level that indicates the system pressure is normal and not under pressure.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let nominal: AVCaptureDevice.SystemPressureState.Level
```

```c
extern AVCaptureSystemPressureLevel const AVCaptureSystemPressureLevelNominal;
```

## See Also

### System pressure levels
- [static let fair: AVCaptureDevice.SystemPressureState.Level](./fair.md)
  A level that indicates that system pressure is slightly elevated.
- [static let serious: AVCaptureDevice.SystemPressureState.Level](./serious.md)
  A level that indicates that system pressure is highly elevated.
- [static let critical: AVCaptureDevice.SystemPressureState.Level](./critical.md)
  System pressure is critically elevated.
- [static let shutdown: AVCaptureDevice.SystemPressureState.Level](./shutdown.md)
  System pressure is beyond critical, so the capture system has shut down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/nominal)*
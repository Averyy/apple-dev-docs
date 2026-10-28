# shutdown

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

System pressure is beyond critical, so the capture system has shut down.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let shutdown: AVCaptureDevice.SystemPressureState.Level
```

```c
extern AVCaptureSystemPressureLevel const AVCaptureSystemPressureLevelShutdown;
```

## Discussion

When system pressure reaches this level, the capture system automatically shuts down, causing a session interruption. Use the [`AVCaptureSessionInterruptionSystemPressureStateKey`](../../../avcapturesessioninterruptionsystempressurestatekey.md) in the interruption notification’s [`userInfo`](../../../../Foundation/notification/userinfo.md) dictionary to find details about the system pressure factors causing the interruption.

## See Also

### System pressure levels
- [static let nominal: AVCaptureDevice.SystemPressureState.Level](./nominal.md)
  A level that indicates the system pressure is normal and not under pressure.
- [static let fair: AVCaptureDevice.SystemPressureState.Level](./fair.md)
  A level that indicates that system pressure is slightly elevated.
- [static let serious: AVCaptureDevice.SystemPressureState.Level](./serious.md)
  A level that indicates that system pressure is highly elevated.
- [static let critical: AVCaptureDevice.SystemPressureState.Level](./critical.md)
  System pressure is critically elevated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/shutdown)*
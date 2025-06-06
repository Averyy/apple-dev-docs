# serious

**Framework**: AVFoundation  
**Kind**: property

A level that indicates that system pressure is highly elevated.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let serious: AVCaptureDevice.SystemPressureState.Level
```

#### Discussion

System pressures may impact capture performance. Consider limiting the frame rate until system pressure state improves.

## See Also

- [static let nominal: AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.struct/nominal.md)
  A level that indicates the system pressure is normal and not under pressure.
- [static let fair: AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.struct/fair.md)
  A level that indicates that system pressure is slightly elevated.
- [static let critical: AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.struct/critical.md)
  System pressure is critically elevated.
- [static let shutdown: AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.struct/shutdown.md)
  System pressure is beyond critical, so the capture system has shut down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/serious)*
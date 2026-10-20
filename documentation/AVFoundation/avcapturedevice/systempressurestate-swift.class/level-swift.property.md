# level

**Framework**: AVFoundation  
**Kind**: property

The overall level of performance constraints on the capture system.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var level: AVCaptureDevice.SystemPressureState.Level { get }
```

#### Discussion

Several aspects of OS and hardware status affect capture system performance and availability (see [`AVCaptureDevice.SystemPressureState.Factors`](avcapturedevice/systempressurestate-swift.class/factors-swift.struct.md)). The overall system pressure level represents the most critical of underlying factors.

## See Also

- [AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.struct.md)
  A structure that defines system pressure state levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.property)*
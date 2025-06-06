# systemPressureState

**Framework**: AVFoundation  
**Kind**: property

A value that indicates the capture device’s current system pressure state.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var systemPressureState: AVCaptureDevice.SystemPressureState { get }
```

#### Discussion

This property indicates whether the capture device is currently in an elevated system pressure condition. When system pressure reaches a [`shutdown`](avcapturedevice/systempressurestate-swift.class/level-swift.struct/shutdown.md) state, the capture device can’t continue to provide input, and the capture session becomes interrupted until the pressured state abates.

You can effectively mitigate system pressure by lowering the device’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) in response to changes in the system pressure state. Implement frame rate throttling to bring system pressure down if your capture use case can tolerate a reduced frame rate.

## See Also

- [AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.class.md)
  An object that provides information about OS and hardware status affecting capture system performance and availability.
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.property)*
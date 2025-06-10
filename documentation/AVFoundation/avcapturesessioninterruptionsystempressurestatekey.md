# AVCaptureSessionInterruptionSystemPressureStateKey

**Framework**: AVFoundation  
**Kind**: var

A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let AVCaptureSessionInterruptionSystemPressureStateKey: String
```

#### Discussion

If an interruption occurs and the value of [`AVCaptureSessionInterruptionReasonKey`](avcapturesessioninterruptionreasonkey.md) equals [`AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure`](avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure.md), the [`userInfo`](https://developer.apple.com/documentation/Foundation/Notification/userInfo) dictionary for the notification contains this key and a corresponding [`AVCaptureDevice.SystemPressureState`](avcapturedevice/systempressurestate-swift.class.md) value.

## See Also

- [var systemPressureState: AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.property.md)
  A value that indicates the capture device’s current system pressure state.
- [AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.class.md)
  An object that provides information about OS and hardware status affecting capture system performance and availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionsystempressurestatekey)*
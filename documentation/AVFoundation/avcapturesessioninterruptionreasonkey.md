# AVCaptureSessionInterruptionReasonKey

**Framework**: AVFoundation  
**Kind**: var

Key to retrieve information about a capture interruption from a [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) user info dictionary.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let AVCaptureSessionInterruptionReasonKey: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a [`AVCaptureSession.InterruptionReason`](avcapturesession/interruptionreason.md) value.

## See Also

- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [AVCaptureSession.InterruptionReason](avcapturesession/interruptionreason.md)
  Constants identifying the reason a capture session was interrupted, found in an [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreasonkey)*
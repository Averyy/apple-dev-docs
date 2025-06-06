# wasInterruptedNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when it interrupts a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class let wasInterruptedNotification: NSNotification.Name
```

#### Discussion

Retrieve the underlying error from the notification’s user information dictionary using the key [`AVCaptureSessionInterruptionReasonKey`](avcapturesessioninterruptionreasonkey.md).

## Topics

### User-Infomation Keys
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [let AVCaptureSessionInterruptionReasonKey: String](avcapturesessioninterruptionreasonkey.md)
  Key to retrieve information about a capture interruption from a [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) user info dictionary.
- [AVCaptureSession.InterruptionReason](avcapturesession/interruptionreason.md)
  Constants identifying the reason a capture session was interrupted, found in an [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) user info dictionary.

## See Also

- [var isRunning: Bool](avcapturesession/isrunning.md)
  A Boolean value that indicates whether the capture session is in a running state.
- [var isInterrupted: Bool](avcapturesession/isinterrupted.md)
  A Boolean value that indicates whether the capture session is in an interrupted state.
- [class let didStartRunningNotification: NSNotification.Name](avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let interruptionEndedNotification: NSNotification.Name](avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.
- [class let runtimeErrorNotification: NSNotification.Name](avcapturesession/runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/wasinterruptednotification)*
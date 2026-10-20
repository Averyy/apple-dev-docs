# wasInterruptedNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSNotificationName const AVCaptureSessionWasInterruptedNotification;
```

#### Discussion

Retrieve the underlying error from the notification’s user information dictionary using the key [`AVCaptureSessionInterruptionReasonKey`](../avcapturesessioninterruptionreasonkey.md).

## Topics

### User-infomation keys
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](../avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [let AVCaptureSessionInterruptionReasonKey: String](../avcapturesessioninterruptionreasonkey.md)
  Key to retrieve information about a capture interruption from a [`wasInterruptedNotification`](./wasinterruptednotification.md) user info dictionary.
- [AVCaptureSession.InterruptionReason](./interruptionreason.md)
  Constants identifying the reason a capture session was interrupted, found in an [`wasInterruptedNotification`](./wasinterruptednotification.md) user info dictionary.

## See Also

### Observing session state
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the capture session is in a running state.
- [var isInterrupted: Bool](./isinterrupted.md)
  A Boolean value that indicates whether the capture session is in an interrupted state.
- [class let didStartRunningNotification: NSNotification.Name](./didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](./didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let interruptionEndedNotification: NSNotification.Name](./interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.
- [class let runtimeErrorNotification: NSNotification.Name](./runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/wasinterruptednotification)*
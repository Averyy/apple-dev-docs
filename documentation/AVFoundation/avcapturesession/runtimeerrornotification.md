# runtimeErrorNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when an error occurs during a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class let runtimeErrorNotification: NSNotification.Name
```

#### Discussion

Retrieve the underlying error from the notification’s user information dictionary using the key [`AVCaptureSessionErrorKey`](avcapturesessionerrorkey.md).

## Topics

### User Info Keys
- [let AVCaptureSessionErrorKey: String](avcapturesessionerrorkey.md)
  Key to retrieve the error object from a [`runtimeErrorNotification`](avcapturesession/runtimeerrornotification.md) user info dictionary.

## See Also

- [var isRunning: Bool](avcapturesession/isrunning.md)
  A Boolean value that indicates whether the capture session is in a running state.
- [var isInterrupted: Bool](avcapturesession/isinterrupted.md)
  A Boolean value that indicates whether the capture session is in an interrupted state.
- [class let didStartRunningNotification: NSNotification.Name](avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let wasInterruptedNotification: NSNotification.Name](avcapturesession/wasinterruptednotification.md)
  A notification the system posts when it interrupts a capture session.
- [class let interruptionEndedNotification: NSNotification.Name](avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/runtimeerrornotification)*
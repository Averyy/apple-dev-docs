# isRunning

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture session is in a running state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isRunning: Bool { get }
```

#### Discussion

This property is key-value observable.

## See Also

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
- [class let runtimeErrorNotification: NSNotification.Name](avcapturesession/runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/isrunning)*
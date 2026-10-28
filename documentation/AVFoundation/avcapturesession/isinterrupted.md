# isInterrupted

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture session is in an interrupted state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isInterrupted: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isInterrupted) BOOL interrupted;
```

## Discussion

This property is key-value observable.

## See Also

### Observing session state
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the capture session is in a running state.
- [class let didStartRunningNotification: NSNotification.Name](./didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](./didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let wasInterruptedNotification: NSNotification.Name](./wasinterruptednotification.md)
  A notification the system posts when it interrupts a capture session.
- [class let interruptionEndedNotification: NSNotification.Name](./interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.
- [class let runtimeErrorNotification: NSNotification.Name](./runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/isinterrupted)*
# prefersInterruptionOnRouteDisconnect

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var prefersInterruptionOnRouteDisconnect: Bool { get }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var prefersNoInterruptionsFromSystemAlerts: Bool](avaudiosession/prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](avaudiosession/setprefersnointerruptionsfromsystemalerts(_:).md)
  Sets the preference for not interrupting the audio session with system alerts.
- [func setPrefersInterruptionOnRouteDisconnect(Bool) throws](avaudiosession/setprefersinterruptiononroutedisconnect(_:).md)
  Sets a preference to interrupt the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/prefersinterruptiononroutedisconnect)*
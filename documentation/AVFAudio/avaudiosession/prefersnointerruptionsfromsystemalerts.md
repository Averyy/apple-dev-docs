# prefersNoInterruptionsFromSystemAlerts

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates a preference for not interrupting the session with system alerts.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
var prefersNoInterruptionsFromSystemAlerts: Bool { get }
```

## See Also

- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](avaudiosession/setprefersnointerruptionsfromsystemalerts(_:).md)
  Sets the preference for not interrupting the audio session with system alerts.
- [var prefersInterruptionOnRouteDisconnect: Bool](avaudiosession/prefersinterruptiononroutedisconnect.md)
  A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [func setPrefersInterruptionOnRouteDisconnect(Bool) throws](avaudiosession/setprefersinterruptiononroutedisconnect(_:).md)
  Sets a preference to interrupt the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/prefersnointerruptionsfromsystemalerts)*
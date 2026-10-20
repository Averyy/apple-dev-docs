# prefersInterruptionOnRouteDisconnect

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL prefersInterruptionOnRouteDisconnect;
```

#### Discussion

The default value is [`true`](../../Swift/true.md).

## See Also

### Handling interruptions
- [var prefersNoInterruptionsFromSystemAlerts: Bool](./prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](./setprefersnointerruptionsfromsystemalerts%28_%29.md)
  Sets the preference for not interrupting the audio session with system alerts.
- [func setPrefersInterruptionOnRouteDisconnect(Bool) throws](./setprefersinterruptiononroutedisconnect%28_%29.md)
  Sets a preference to interrupt the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](./interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/prefersinterruptiononroutedisconnect)*
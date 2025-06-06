# setPrefersInterruptionOnRouteDisconnect(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets a preference to interrupt the audio session when the active route disconnects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func setPrefersInterruptionOnRouteDisconnect(_ inValue: Bool) throws
```

#### Discussion

The expected behavior of an app is to pause playback if a route change occurs due to a device no longer being available ([`AVAudioSession.RouteChangeReason.oldDeviceUnavailable`](avaudiosession/routechangereason/olddeviceunavailable.md)). Starting in iOS 17, the system interrupts active Now Playing sessions when a route change occurs due to a disconnection event, but doesn’t interrupt other sessions.

## Parameters

- `inValue`: Specify a   value to opt out of interruption on route disconnect. Set to   to reset to the default behavior.

## See Also

- [var prefersNoInterruptionsFromSystemAlerts: Bool](avaudiosession/prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](avaudiosession/setprefersnointerruptionsfromsystemalerts(_:).md)
  Sets the preference for not interrupting the audio session with system alerts.
- [var prefersInterruptionOnRouteDisconnect: Bool](avaudiosession/prefersinterruptiononroutedisconnect.md)
  A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setprefersinterruptiononroutedisconnect(_:))*
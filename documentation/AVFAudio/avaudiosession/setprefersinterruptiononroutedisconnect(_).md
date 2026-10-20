# setPrefersInterruptionOnRouteDisconnect(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setPrefersInterruptionOnRouteDisconnect:(BOOL) inValue error:(NSError **) outError;
```

#### Discussion

The expected behavior of an app is to pause playback if a route change occurs due to a device no longer being available ([`AVAudioSession.RouteChangeReason.oldDeviceUnavailable`](./routechangereason/olddeviceunavailable.md)). Starting in iOS 17, the system interrupts active Now Playing sessions when a route change occurs due to a disconnection event, but doesn’t interrupt other sessions.

## Parameters

- `inValue`: Specify a [`false`](../../Swift/false.md) value to opt out of interruption on route disconnect. Set to [`true`](../../Swift/true.md) to reset to the default behavior.

## See Also

### Handling interruptions
- [var prefersNoInterruptionsFromSystemAlerts: Bool](./prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](./setprefersnointerruptionsfromsystemalerts%28_%29.md)
  Sets the preference for not interrupting the audio session with system alerts.
- [var prefersInterruptionOnRouteDisconnect: Bool](./prefersinterruptiononroutedisconnect.md)
  A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](./interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setprefersinterruptiononroutedisconnect(_:))*
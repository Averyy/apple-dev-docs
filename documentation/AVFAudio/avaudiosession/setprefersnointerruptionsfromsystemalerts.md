# setPrefersNoInterruptionsFromSystemAlerts(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the preference for not interrupting the audio session with system alerts.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
func setPrefersNoInterruptionsFromSystemAlerts(_ inValue: Bool) throws
```

## Mentions

- [Handling audio interruptions](handling-audio-interruptions.md)

#### Discussion

Beginning in iOS 14, users can set a global preference that indicates whether the system displays incoming calls using a banner or a full-screen display style. If using the banner style, setting this value to [`true`](https://developer.apple.com/documentation/swift/true) prevents the system from interrupting the audio session with incoming call notifications, and gives the user an opportunity to accept or decline the call. The system only interrupts the audio session if the user accepts the call.

Enabling this preference can improve the user experience of apps with audio sessions that you don’t want to interrupt, such as those that record audiovisual media or that you use for music performance.

> ❗ **Important**:  This preference has no effect if the device uses the full-screen display style—the system interrupts the audio session on incoming calls.

## Parameters

- `inValue`: The interruption preference value.

## See Also

- [var prefersNoInterruptionsFromSystemAlerts: Bool](avaudiosession/prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [var prefersInterruptionOnRouteDisconnect: Bool](avaudiosession/prefersinterruptiononroutedisconnect.md)
  A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [func setPrefersInterruptionOnRouteDisconnect(Bool) throws](avaudiosession/setprefersinterruptiononroutedisconnect(_:).md)
  Sets a preference to interrupt the audio session when the active route disconnects.
- [class let interruptionNotification: NSNotification.Name](avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setprefersnointerruptionsfromsystemalerts(_:))*
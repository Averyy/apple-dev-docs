# routeChangeNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when its audio route changes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let routeChangeNotification: NSNotification.Name
```

## Mentions

- [Responding to audio route changes](responding-to-audio-route-changes.md)

#### Discussion

The [`userInfo`](https://developer.apple.com/documentation/Foundation/NSNotification/userInfo) dictionary of this notification contains the [`AVAudioSessionRouteChangeReasonKey`](avaudiosessionroutechangereasonkey.md) and [`AVAudioSessionRouteChangePreviousRouteKey`](avaudiosessionroutechangepreviousroutekey.md) keys, which provide information about the route change.

See [`Responding to audio route changes`](responding-to-audio-route-changes.md) for more information on using this notification.

The system posts this notification on a secondary thread.

## Topics

### User Info Keys
- [let AVAudioSessionRouteChangeReasonKey: String](avaudiosessionroutechangereasonkey.md)
  A user info key that’s used to retrieve the route change reason.
- [let AVAudioSessionRouteChangePreviousRouteKey: String](avaudiosessionroutechangepreviousroutekey.md)
  A user info key that’s used to retrieve the previously active audio session route.
### User Info Values
- [AVAudioSession.RouteChangeReason](avaudiosession/routechangereason.md)
  Constants that indicate the reason for an audio route change.

## See Also

- [var currentRoute: AVAudioSessionRouteDescription](avaudiosession/currentroute.md)
  A description of the current audio route’s input and output ports.
- [class AVAudioSessionRouteDescription](avaudiosessionroutedescription.md)
  An object that describes the input and output ports associated with a session’s audio route.
- [class AVAudioSessionPortDescription](avaudiosessionportdescription.md)
  Information about the capabilities of the port and the hardware channels it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routechangenotification)*
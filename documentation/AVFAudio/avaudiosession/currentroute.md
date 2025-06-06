# currentRoute

**Framework**: AVFAudio  
**Kind**: property

A description of the current audio route’s input and output ports.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var currentRoute: AVAudioSessionRouteDescription { get }
```

## Mentions

- [Responding to audio route changes](responding-to-audio-route-changes.md)

#### Discussion

An audio route is an electronic pathway for audio signals. Inspect the state of device audio routes and configure your preferred input and output route settings.

## See Also

- [class AVAudioSessionRouteDescription](avaudiosessionroutedescription.md)
  An object that describes the input and output ports associated with a session’s audio route.
- [class AVAudioSessionPortDescription](avaudiosessionportdescription.md)
  Information about the capabilities of the port and the hardware channels it supports.
- [class let routeChangeNotification: NSNotification.Name](avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/currentroute)*
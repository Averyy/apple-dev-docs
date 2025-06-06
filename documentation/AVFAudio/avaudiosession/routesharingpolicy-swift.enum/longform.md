# longForm

**Framework**: AVFAudio  
**Kind**: property

A policy that routes output to the shared long-form audio output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var longForm: AVAudioSession.RouteSharingPolicy { get }
```

#### Discussion

An audio session whose primary use case is as a music or podcast player may use this value to play to the same output as the Music and Podcasts apps. All applications on the system that use this policy have their audio routed to the same location.

## See Also

- [AVAudioSession.RouteSharingPolicy.default](avaudiosession/routesharingpolicy-swift.enum/default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [AVAudioSession.RouteSharingPolicy.independent](avaudiosession/routesharingpolicy-swift.enum/independent.md)
  A policy in which the route picker UI directs videos to a wireless route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/longform)*
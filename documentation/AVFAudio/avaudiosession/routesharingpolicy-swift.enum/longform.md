# longForm

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A policy that routes output to the shared long-form audio output.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0 (renamed: AVAudioSession.RouteSharingPolicy.longFormAudio)
- iPadOS 11.0+ - Deprecated in 13.0 (renamed: AVAudioSession.RouteSharingPolicy.longFormAudio)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: AVAudioSession.RouteSharingPolicy.longFormAudio)
- tvOS 11.0+ - Deprecated in 13.0 (renamed: AVAudioSession.RouteSharingPolicy.longFormAudio)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AVAudioSession.RouteSharingPolicy.longFormAudio)
- watchOS 4.0+ - Deprecated in 6.0 (renamed: AVAudioSession.RouteSharingPolicy.longFormAudio)

> **Deprecated**: Use [`AVAudioSession.RouteSharingPolicy.longFormAudio`](./longformaudio.md) instead.

## Declaration

```swift
static var longForm: AVAudioSession.RouteSharingPolicy { get }
```

```c
AVAudioSessionRouteSharingPolicyLongForm
```

#### Discussion

An audio session whose primary use case is as a music or podcast player may use this value to play to the same output as the Music and Podcasts apps. All applications on the system that use this policy have their audio routed to the same location.

## See Also

### Choosing a route-sharing policy
- [AVAudioSession.RouteSharingPolicy.default](./default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](./longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](./longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [AVAudioSession.RouteSharingPolicy.independent](./independent.md)
  A policy in which the route picker UI directs videos to a wireless route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/longform)*
# AVAudioSession.RouteSharingPolicy.independent

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A policy in which the route picker UI directs videos to a wireless route.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case independent
```

```c
AVAudioSessionRouteSharingPolicyIndependent
```

#### Discussion

In iOS, the system sets this policy in cases where the user directs video to a wireless route using the route picker UI. Apps shouldn’t try to set this value directly.

## See Also

### Choosing a route-sharing policy
- [AVAudioSession.RouteSharingPolicy.default](./default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](./longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](./longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [static var longForm: AVAudioSession.RouteSharingPolicy](./longform.md)
  A policy that routes output to the shared long-form audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/independent)*
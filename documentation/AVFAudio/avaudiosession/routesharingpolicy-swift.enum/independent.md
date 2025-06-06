# AVAudioSession.RouteSharingPolicy.independent

**Framework**: AVFAudio  
**Kind**: case

A policy in which the route picker UI directs videos to a wireless route.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case independent
```

#### Discussion

In iOS, the system sets this policy in cases where the user directs video to a wireless route using the route picker UI. Apps shouldn’t try to set this value directly.

## See Also

- [AVAudioSession.RouteSharingPolicy.default](avaudiosession/routesharingpolicy-swift.enum/default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [static var longForm: AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.enum/longform.md)
  A policy that routes output to the shared long-form audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/independent)*
# AVAudioSession.RouteSharingPolicy.longFormVideo

**Framework**: AVFAudio  
**Kind**: case

A policy that routes output to the shared long-form video output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case longFormVideo
```

#### Discussion

Apps that play long-form video content can use this policy to play to the same output as other long-form video apps, such as the built-in TV app. These apps should also set the `AVInitialRouteSharingPolicy` key in their `Info.plist` to `LongFormVideo`. Video content not using this route sharing policy remains local to the playback device even when the system is routing long-form video content to AirPlay.

## See Also

- [AVAudioSession.RouteSharingPolicy.default](avaudiosession/routesharingpolicy-swift.enum/default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.independent](avaudiosession/routesharingpolicy-swift.enum/independent.md)
  A policy in which the route picker UI directs videos to a wireless route.
- [static var longForm: AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.enum/longform.md)
  A policy that routes output to the shared long-form audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/longformvideo)*
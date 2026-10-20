# AVAudioSession.RouteSharingPolicy.longFormVideo

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

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

```c
AVAudioSessionRouteSharingPolicyLongFormVideo
```

#### Discussion

Apps that play long-form video content can use this policy to play to the same output as other long-form video apps, such as the built-in TV app. These apps should also set the `AVInitialRouteSharingPolicy` key in their `Info.plist` to `LongFormVideo`. Video content not using this route sharing policy remains local to the playback device even when the system is routing long-form video content to AirPlay.

## See Also

### Choosing a route-sharing policy
- [AVAudioSession.RouteSharingPolicy.default](./default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](./longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.independent](./independent.md)
  A policy in which the route picker UI directs videos to a wireless route.
- [static var longForm: AVAudioSession.RouteSharingPolicy](./longform.md)
  A policy that routes output to the shared long-form audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/longformvideo)*
# AVAudioSession.RouteSharingPolicy.longFormAudio

**Framework**: AVFAudio  
**Kind**: case

A policy that routes output to the shared long-form audio output.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case longFormAudio
```

#### Discussion

Apps that play long-form audio, such as music or audio books, can use this policy to play to the same output as the built-in Music and Podcast apps. Long-form audio apps should also use the [`Media Player`](https://developer.apple.com/documentation/MediaPlayer) framework to add support for remote control events and to provide Now Playing information.

Apps running in watchOS that use this policy are able to play audio in the background, as long as the audio session can activate an eligible audio route. These apps must activate their audio session using the [`activate(options:completionHandler:)`](avaudiosession/activate(options:completionhandler:).md) method. This ensures that the user has the opportunity to pick an appropriate audio route when the audio session can’t select one automatically.

## See Also

- [AVAudioSession.RouteSharingPolicy.default](avaudiosession/routesharingpolicy-swift.enum/default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [AVAudioSession.RouteSharingPolicy.independent](avaudiosession/routesharingpolicy-swift.enum/independent.md)
  A policy in which the route picker UI directs videos to a wireless route.
- [static var longForm: AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.enum/longform.md)
  A policy that routes output to the shared long-form audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum/longformaudio)*
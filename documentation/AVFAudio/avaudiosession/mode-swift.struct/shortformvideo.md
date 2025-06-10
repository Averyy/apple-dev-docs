# shortFormVideo

**Framework**: AVFAudio  
**Kind**: property

Appropriate for applications playing short-form video content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
static let shortFormVideo: AVAudioSession.Mode
```

#### Discussion

Only valid with [`playback`](avaudiosession/category-swift.struct/playback.md). Not applicable with [`AVAudioSession.RouteSharingPolicy.longFormAudio`](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md), or [`AVAudioSession.RouteSharingPolicy.longFormVideo`](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md).

When this mode is set:

- system will make informed decisions to automatically unmute the output of the media if the user shows intention of unmuting. - When auto-unmuted, [`userIntentToUnmuteOutputNotification`](avaudiosession/userintenttounmuteoutputnotification.md) and [`outputMuteStateChangeNotification`](avaudiosession/outputmutestatechangenotification.md) will be sent.
- if the session is output muted, system may prevent interrupting other active audio apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/shortformvideo)*
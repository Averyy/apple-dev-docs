# audioOutputSuppressedDueToNonMixableAudioRoute

**Framework**: AVFoundation  
**Kind**: property

Whether the player’s audio output is suppressed due to being on a non-mixable audio route.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var audioOutputSuppressedDueToNonMixableAudioRoute: Bool { get }
```

#### Discussion

If YES, the player’s audio output is suppressed. The player is muted while on a non-mixable audio route and cannot play audio. The player’s mute property does not reflect the true mute status. If NO, the player’s audio output is not suppressed. The player may be muted or unmuted while on a non-mixable audio route and can play audio. The player’s mute property reflects the true mute status. In a non-mixable audio route, only one player can play audio. To play audio in non-mixable states, the player must be specified as the priority participant in AVRoutingPlaybackArbiter.preferredParticipantForNonMixableAudioRoutes. If this player becomes the preferred player, it will gain audio priority and suppress the audio of all other players. If another participant becomes the preferred participant, this player will lose audio priority and have their audio suppressed. This property is key-value observed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/audiooutputsuppressedduetononmixableaudioroute)*
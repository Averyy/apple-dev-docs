# allowsExternalPlayback

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the player allows switching to external playback mode.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+

## Declaration

```swift
nonisolated
var allowsExternalPlayback: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var isExternalPlaybackActive: Bool](avplayer/isexternalplaybackactive.md)
  A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [var usesExternalPlaybackWhileExternalScreenIsActive: Bool](avplayer/usesexternalplaybackwhileexternalscreenisactive.md)
  A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.
- [var externalPlaybackVideoGravity: AVLayerVideoGravity](avplayer/externalplaybackvideogravity.md)
  The video gravity of the player for external playback mode only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/allowsexternalplayback)*
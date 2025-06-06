# externalPlaybackVideoGravity

**Framework**: AVFoundation  
**Kind**: property

The video gravity of the player for external playback mode only.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
nonisolated
var externalPlaybackVideoGravity: AVLayerVideoGravity { get set }
```

#### Discussion

Valid values are [`resize`](avlayervideogravity/resize.md), [`resizeAspectFill`](avlayervideogravity/resizeaspectfill.md), or [`resizeAspect`](avlayervideogravity/resizeaspect.md).

## See Also

- [var allowsExternalPlayback: Bool](avplayer/allowsexternalplayback.md)
  A Boolean value that indicates whether the player allows switching to external playback mode.
- [var isExternalPlaybackActive: Bool](avplayer/isexternalplaybackactive.md)
  A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [var usesExternalPlaybackWhileExternalScreenIsActive: Bool](avplayer/usesexternalplaybackwhileexternalscreenisactive.md)
  A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/externalplaybackvideogravity)*
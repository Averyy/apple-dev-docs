# usesExternalPlaybackWhileExternalScreenIsActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
nonisolated
var usesExternalPlaybackWhileExternalScreenIsActive: Bool { get set }
```

```objc
@property BOOL usesExternalPlaybackWhileExternalScreenIsActive;
```

## Discussion

The player automatically switches back to the external screen mode once video playback concludes. A brief transition may be visible on the external display when automatically switching between the two modes. The default value of this property is [`false`](../../Swift/false.md). The value of this property has no effect if [`allowsExternalPlayback`](./allowsexternalplayback.md) is [`false`](../../Swift/false.md).

## See Also

### Managing external playback
- [var allowsExternalPlayback: Bool](./allowsexternalplayback.md)
  A Boolean value that indicates whether the player allows switching to external playback mode.
- [var isExternalPlaybackActive: Bool](./isexternalplaybackactive.md)
  A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [var externalPlaybackVideoGravity: AVLayerVideoGravity](./externalplaybackvideogravity.md)
  The video gravity of the player for external playback mode only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/usesexternalplaybackwhileexternalscreenisactive)*
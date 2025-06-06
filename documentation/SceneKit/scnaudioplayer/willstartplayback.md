# willStartPlayback

**Framework**: SceneKit  
**Kind**: property

A block called by SceneKit when playback of the player’s audio source is about to begin.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var willStartPlayback: (() -> Void)? { get set }
```

#### Discussion

The block takes no parameters and returns no value. Use this block to perform actions in response to the playing of sounds.

## See Also

- [var didFinishPlayback: (() -> Void)?](scnaudioplayer/didfinishplayback.md)
  A block called by SceneKit when playback of the player’s audio source has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/willstartplayback)*
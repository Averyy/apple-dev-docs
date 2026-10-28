# didFinishPlayback

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A block called by SceneKit when playback of the player’s audio source has completed.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var didFinishPlayback: (() -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^didFinishPlayback)();
```

## Discussion

The block takes no parameters and returns no value. Use this block to perform actions when a sound finishes playing. For example, after a line of spoken character dialogue finishes playing, you might start playing another line of dialogue.

## See Also

### Responding to Playback
- [var willStartPlayback: (() -> Void)?](./willstartplayback.md)
  A block called by SceneKit when playback of the player’s audio source is about to begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/didfinishplayback)*
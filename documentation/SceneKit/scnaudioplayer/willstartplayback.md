# willStartPlayback

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A block called by SceneKit when playback of the player’s audio source is about to begin.

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
var willStartPlayback: (() -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^willStartPlayback)();
```

#### Discussion

The block takes no parameters and returns no value. Use this block to perform actions in response to the playing of sounds.

## See Also

### Responding to Playback
- [var didFinishPlayback: (() -> Void)?](./didfinishplayback.md)
  A block called by SceneKit when playback of the player’s audio source has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/willstartplayback)*
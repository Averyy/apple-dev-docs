# isPlaying

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that determines whether the scene is playing.

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
var isPlaying: Bool { get set }
```

```objc
@property (getter=isPlaying) BOOL playing;
```

#### Discussion

If the value of this property is [`false`](../../Swift/false.md) (the default), SceneKit does not increment the scene time, so animations associated with the scene do not play. Change this property’s value to [`true`](../../Swift/true.md) to start animating the scene.

## See Also

### Managing Scene Animation Timing
- [var sceneTime: TimeInterval](./scenetime.md)
  The current scene time.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/isplaying)*
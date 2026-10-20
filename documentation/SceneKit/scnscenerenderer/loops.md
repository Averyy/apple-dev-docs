# loops

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.

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
var loops: Bool { get set }
```

```objc
@property (nonatomic) BOOL loops;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md) (the default), SceneKit returns the scene time to zero after all animations associated with the scene have played, causing those animations to repeat. Otherwise, SceneKit stops playing the scene when all animations have completed.

## See Also

### Managing Scene Animation Timing
- [var sceneTime: TimeInterval](./scenetime.md)
  The current scene time.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that determines whether the scene is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/loops)*
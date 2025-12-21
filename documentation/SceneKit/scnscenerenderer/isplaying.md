# isPlaying

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether the scene is playing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isPlaying: Bool { get set }
```

#### Discussion

If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), SceneKit does not increment the scene time, so animations associated with the scene do not play. Change this property’s value to [`true`](https://developer.apple.com/documentation/Swift/true) to start animating the scene.

## See Also

- [var sceneTime: TimeInterval](scnscenerenderer/scenetime.md)
  The current scene time.
- [var loops: Bool](scnscenerenderer/loops.md)
  A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/isplaying)*
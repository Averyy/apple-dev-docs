# loops

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.

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
var loops: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) (the default), SceneKit returns the scene time to zero after all animations associated with the scene have played, causing those animations to repeat. Otherwise, SceneKit stops playing the scene when all animations have completed.

## See Also

- [var sceneTime: TimeInterval](scnscenerenderer/scenetime.md)
  The current scene time.
- [var isPlaying: Bool](scnscenerenderer/isplaying.md)
  A Boolean value that determines whether the scene is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/loops)*
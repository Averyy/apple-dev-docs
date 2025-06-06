# isPlaying

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that determines whether the scene is playing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isPlaying: Bool { get set }
```

#### Discussion

If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false) (the default), SceneKit does not increment the scene time, so animations associated with the scene do not play. Change this property’s value to [`true`](https://developer.apple.com/documentation/swift/true) to start animating the scene.

## See Also

- [var loops: Bool](sk3dnode/loops.md)
  A Boolean value that determines whether Scene Kit restarts the scene time after all animations in the scene have played.
- [var sceneTime: TimeInterval](sk3dnode/scenetime.md)
  The current scene time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/isplaying)*
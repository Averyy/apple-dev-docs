# sceneTime

**Framework**: SpriteKit  
**Kind**: property

The current scene time.

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
var sceneTime: TimeInterval { get set }
```

#### Discussion

This timestamp determines the behavior of running animations, similar to how the playhead time in a video player application determines which frame of a movie to display. It applies only to animations whose [`usesSceneTimeBase`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/usesSceneTimeBase) property is [`true`](https://developer.apple.com/documentation/swift/true), including those loaded from a scene source using the [`playUsingSceneTimeBase`](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/1523222-playusingscenetimebase) option.

Use this property together with the above animation options when you want to directly control (or allow the user to directly control) the playback of animations.

## See Also

- [var isPlaying: Bool](sk3dnode/isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var loops: Bool](sk3dnode/loops.md)
  A Boolean value that determines whether Scene Kit restarts the scene time after all animations in the scene have played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/scenetime)*
# sceneTime

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The current scene time.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var sceneTime: TimeInterval { get set }
```

#### Discussion

This timestamp determines how running animations behave, which is similar to how the playhead time in a video player application determines which frame of a movie to display. Scene time applies only to animations whose [`usesSceneTimeBase`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/usesSceneTimeBase) property is [`true`](https://developer.apple.com/documentation/swift/true), including those loaded from a scene source using the [`playUsingSceneTimeBase`](scnscenesource/animationimportpolicy/playusingscenetimebase.md) option.

Use this property, together with the above animation options, when you want to directly control (or allow the user to directly control) the playback of animations. For example, if you’re building an authoring tool for 3D assets, you might bind this property’s value to a slider control for scrubbing through playback of animations in a scene file.

## See Also

- [var isPlaying: Bool](scnscenerenderer/isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var loops: Bool](scnscenerenderer/loops.md)
  A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/scenetime)*
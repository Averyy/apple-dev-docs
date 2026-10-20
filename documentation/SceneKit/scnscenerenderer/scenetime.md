# sceneTime

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The current scene time.

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
var sceneTime: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval sceneTime;
```

#### Discussion

This timestamp determines how running animations behave, which is similar to how the playhead time in a video player application determines which frame of a movie to display. Scene time applies only to animations whose [`usesSceneTimeBase`](../../QuartzCore/caanimation/usesscenetimebase.md) property is [`true`](../../Swift/true.md), including those loaded from a scene source using the [`playUsingSceneTimeBase`](../scnscenesource/animationimportpolicy/playusingscenetimebase.md) option.

Use this property, together with the above animation options, when you want to directly control (or allow the user to directly control) the playback of animations. For example, if you’re building an authoring tool for 3D assets, you might bind this property’s value to a slider control for scrubbing through playback of animations in a scene file.

## See Also

### Managing Scene Animation Timing
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/scenetime)*
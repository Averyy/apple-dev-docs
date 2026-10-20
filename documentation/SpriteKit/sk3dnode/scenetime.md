# sceneTime

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The current scene time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sceneTime: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval sceneTime;
```

#### Discussion

This timestamp determines the behavior of running animations, similar to how the playhead time in a video player application determines which frame of a movie to display. It applies only to animations whose [`usesSceneTimeBase`](../../QuartzCore/caanimation/usesscenetimebase.md) property is [`true`](../../Swift/true.md), including those loaded from a scene source using the [`playUsingSceneTimeBase`](../../SceneKit/scnscenesource/animationimportpolicy/playusingscenetimebase.md) option.

Use this property together with the above animation options when you want to directly control (or allow the user to directly control) the playback of animations.

## See Also

### Animating a 3D Node’s Content in Scene Kit
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether Scene Kit restarts the scene time after all animations in the scene have played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/scenetime)*
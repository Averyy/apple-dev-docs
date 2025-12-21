# playUsingSceneTimeBase

**Framework**: SceneKit  
**Kind**: property

Animations loaded from the scene file are immediately added to the scene and played according to the scene’s [`sceneTime`](scnscenerenderer/scenetime.md) property.

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
static let playUsingSceneTimeBase: SCNSceneSource.AnimationImportPolicy
```

#### Discussion

Using this policy is equivalent to manually loading each animation, setting its [`usesSceneTimeBase`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/usesSceneTimeBase) property to [`true`](https://developer.apple.com/documentation/Swift/true), and adding it to the appropriate element of the scene. Use this policy when you want to directly control (or let the user directly control) the progress of animations.

## See Also

- [static let doNotPlay: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/donotplay.md)
  Animations are not loaded from the scene file.
- [static let play: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/play.md)
  Animations loaded from the scene file are immediately added to the scene and played once.
- [static let playRepeatedly: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/playrepeatedly.md)
  Animations loaded from the scene file are immediately added to the scene and played repeatedly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/playusingscenetimebase)*
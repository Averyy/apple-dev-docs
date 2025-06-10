# play

**Framework**: SceneKit  
**Kind**: property

Animations loaded from the scene file are immediately added to the scene and played once.

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
static let play: SCNSceneSource.AnimationImportPolicy
```

#### Discussion

Using this policy is equivalent to manually loading each animation, setting its [`repeatCount`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/repeatCount) property to `1`, and adding it to the appropriate element of the scene.

## See Also

- [static let doNotPlay: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/donotplay.md)
  Animations are not loaded from the scene file.
- [static let playRepeatedly: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/playrepeatedly.md)
  Animations loaded from the scene file are immediately added to the scene and played repeatedly.
- [static let playUsingSceneTimeBase: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/playusingscenetimebase.md)
  Animations loaded from the scene file are immediately added to the scene and played according to the scene’s [`sceneTime`](scnscenerenderer/scenetime.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/play)*
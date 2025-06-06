# playRepeatedly

**Framework**: SceneKit  
**Kind**: property

Animations loaded from the scene file are immediately added to the scene and played repeatedly.

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
static let playRepeatedly: SCNSceneSource.AnimationImportPolicy
```

#### Discussion

Using this policy is equivalent to manually loading each animation, setting its [`repeatCount`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/repeatCount) property to `INFINITY`, and adding it to the appropriate element of the scene.

## See Also

- [static let doNotPlay: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/donotplay.md)
  Animations are not loaded from the scene file.
- [static let play: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/play.md)
  Animations loaded from the scene file are immediately added to the scene and played once.
- [static let playUsingSceneTimeBase: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/playusingscenetimebase.md)
  Animations loaded from the scene file are immediately added to the scene and played according to the scene’s [`sceneTime`](scnscenerenderer/scenetime.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/playrepeatedly)*
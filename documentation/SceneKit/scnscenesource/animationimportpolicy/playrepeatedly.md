# playRepeatedly

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Animations loaded from the scene file are immediately added to the scene and played repeatedly.

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
static let playRepeatedly: SCNSceneSource.AnimationImportPolicy
```

```c
extern SCNSceneSourceAnimationImportPolicy const SCNSceneSourceAnimationImportPolicyPlayRepeatedly;
```

#### Discussion

Using this policy is equivalent to manually loading each animation, setting its [`repeatCount`](../../../QuartzCore/camediatiming/repeatcount.md) property to `INFINITY`, and adding it to the appropriate element of the scene.

## See Also

### Type Properties
- [static let doNotPlay: SCNSceneSource.AnimationImportPolicy](./donotplay.md)
  Animations are not loaded from the scene file.
- [static let play: SCNSceneSource.AnimationImportPolicy](./play.md)
  Animations loaded from the scene file are immediately added to the scene and played once.
- [static let playUsingSceneTimeBase: SCNSceneSource.AnimationImportPolicy](./playusingscenetimebase.md)
  Animations loaded from the scene file are immediately added to the scene and played according to the scene’s [`sceneTime`](../../scnscenerenderer/scenetime.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/playrepeatedly)*
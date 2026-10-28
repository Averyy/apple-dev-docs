# doNotPlay

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Animations are not loaded from the scene file.

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
static let doNotPlay: SCNSceneSource.AnimationImportPolicy
```

```c
extern SCNSceneSourceAnimationImportPolicy const SCNSceneSourceAnimationImportPolicyDoNotPlay;
```

## Discussion

To play animations stored in the scene file, load them manually using the [`entryWithIdentifier:withClass:`](../entrywithidentifier_withclass_.md) method.

## See Also

### Type Properties
- [static let play: SCNSceneSource.AnimationImportPolicy](./play.md)
  Animations loaded from the scene file are immediately added to the scene and played once.
- [static let playRepeatedly: SCNSceneSource.AnimationImportPolicy](./playrepeatedly.md)
  Animations loaded from the scene file are immediately added to the scene and played repeatedly.
- [static let playUsingSceneTimeBase: SCNSceneSource.AnimationImportPolicy](./playusingscenetimebase.md)
  Animations loaded from the scene file are immediately added to the scene and played according to the scene’s [`sceneTime`](../../scnscenerenderer/scenetime.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/donotplay)*
# doNotPlay

**Framework**: SceneKit  
**Kind**: property

Animations are not loaded from the scene file.

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
static let doNotPlay: SCNSceneSource.AnimationImportPolicy
```

#### Discussion

To play animations stored in the scene file, load them manually using the [`entryWithIdentifier:withClass:`](scnscenesource/entrywithidentifier:withclass:.md) method.

## See Also

- [static let play: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/play.md)
  Animations loaded from the scene file are immediately added to the scene and played once.
- [static let playRepeatedly: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/playrepeatedly.md)
  Animations loaded from the scene file are immediately added to the scene and played repeatedly.
- [static let playUsingSceneTimeBase: SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy/playusingscenetimebase.md)
  Animations loaded from the scene file are immediately added to the scene and played according to the scene’s [`sceneTime`](scnscenerenderer/scenetime.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/animationimportpolicy/donotplay)*
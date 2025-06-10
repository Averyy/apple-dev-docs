# animationImportPolicy

**Framework**: SceneKit  
**Kind**: property

An option for controlling the playback of animations in a scene file.

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
static let animationImportPolicy: SCNSceneSource.LoadingOption
```

#### Discussion

The value for this key is one of the constants listed in `Animation Import Policies`.

The default value for this key is [`playRepeatedly`](scnscenesource/animationimportpolicy/playrepeatedly.md). For apps built for 10.9 or earlier, the default value is [`playUsingSceneTimeBase`](scnscenesource/animationimportpolicy/playusingscenetimebase.md).

## See Also

- [SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy.md)
  Options for playing animations loaded from a scene file, used with the [`animationImportPolicy`](scnscenesource/loadingoption/animationimportpolicy.md) key in options dictionaries.
- [static let assetDirectoryURLs: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/assetdirectoryurls.md)
  Locations to use for resolving relative URLs to external resources.
- [static let checkConsistency: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/checkconsistency.md)
  An option to validate scene files while loading.
- [static let convertToYUp: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/converttoyup.md)
  An option for whether to transform assets loaded from the scene file for use in a coordinate system where the y-axis points up.
- [static let convertUnitsToMeters: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/convertunitstometers.md)
  An option for whether to automatically scale the scene’s contents.
- [static let createNormalsIfAbsent: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/createnormalsifabsent.md)
  An option for automatically generating surface normals if they are absent when loading geometry.
- [static let flattenScene: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/flattenscene.md)
  An option for automatically merging portions of a scene graph during loading.
- [static let overrideAssetURLs: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/overrideasseturls.md)
  An option to attempt loading external resources using their URLs as specified in a scene file.
- [static let preserveOriginalTopology: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/preserveoriginaltopology.md)
- [static let strictConformance: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/strictconformance.md)
  An option to interpret scene files exactly as specified by the scene file format.
- [static let useSafeMode: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/usesafemode.md)
  An option to limit filesystem and network access for external resources referenced by a scene file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/animationimportpolicy)*
# createNormalsIfAbsent

**Framework**: SceneKit  
**Kind**: property

An option for automatically generating surface normals if they are absent when loading geometry.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let createNormalsIfAbsent: SCNSceneSource.LoadingOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

To participate in lighting and shading, a geometry must include surface normal vectors in its vertex data. Some scene files may not contain such data. If you set this option’s value to [`true`](https://developer.apple.com/documentation/swift/true), SceneKit applies heuristics to generate surface normal data for each geometry it loads from the scene source if such data is absent.

## See Also

- [static let animationImportPolicy: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/animationimportpolicy.md)
  An option for controlling the playback of animations in a scene file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/createnormalsifabsent)*
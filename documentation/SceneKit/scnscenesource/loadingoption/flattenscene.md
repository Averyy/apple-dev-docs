# flattenScene

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option for automatically merging portions of a scene graph during loading.

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
static let flattenScene: SCNSceneSource.LoadingOption
```

```c
extern SCNSceneSourceLoadingOption const SCNSceneSourceFlattenSceneKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object containing a Boolean value. The default value is [`false`](../../../Swift/false.md).

If you set this option’s value to [`true`](../../../Swift/true.md), SceneKit attempts to reduce the complexity of the scene graph loaded from the scene source by merging geometries and combining nodes. Use this option for more efficient rendering when manipulation of the scene graph is not needed (for example, when rendering a quick preview of a scene’s contents).

## See Also

### Type Properties
- [static let animationImportPolicy: SCNSceneSource.LoadingOption](./animationimportpolicy.md)
  An option for controlling the playback of animations in a scene file.
- [SCNSceneSource.AnimationImportPolicy](../animationimportpolicy.md)
  Options for playing animations loaded from a scene file, used with the [`animationImportPolicy`](./animationimportpolicy.md) key in options dictionaries.
- [static let assetDirectoryURLs: SCNSceneSource.LoadingOption](./assetdirectoryurls.md)
  Locations to use for resolving relative URLs to external resources.
- [static let checkConsistency: SCNSceneSource.LoadingOption](./checkconsistency.md)
  An option to validate scene files while loading.
- [static let convertToYUp: SCNSceneSource.LoadingOption](./converttoyup.md)
  An option for whether to transform assets loaded from the scene file for use in a coordinate system where the y-axis points up.
- [static let convertUnitsToMeters: SCNSceneSource.LoadingOption](./convertunitstometers.md)
  An option for whether to automatically scale the scene’s contents.
- [static let createNormalsIfAbsent: SCNSceneSource.LoadingOption](./createnormalsifabsent.md)
  An option for automatically generating surface normals if they are absent when loading geometry.
- [static let overrideAssetURLs: SCNSceneSource.LoadingOption](./overrideasseturls.md)
  An option to attempt loading external resources using their URLs as specified in a scene file.
- [static let preserveOriginalTopology: SCNSceneSource.LoadingOption](./preserveoriginaltopology.md)
- [static let strictConformance: SCNSceneSource.LoadingOption](./strictconformance.md)
  An option to interpret scene files exactly as specified by the scene file format.
- [static let useSafeMode: SCNSceneSource.LoadingOption](./usesafemode.md)
  An option to limit filesystem and network access for external resources referenced by a scene file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/flattenscene)*
# convertToYUp

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option for whether to transform assets loaded from the scene file for use in a coordinate system where the y-axis points up.

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
static let convertToYUp: SCNSceneSource.LoadingOption
```

```c
extern SCNSceneSourceLoadingOption const SCNSceneSourceConvertToYUpKey;
```

## Discussion

The value for this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object containing a Boolean value. The default value is [`false`](../../../Swift/false.md).

SceneKit’s physics simulation works best when the y-axis of scene coordinate space corresponds to the “up” direction of the physics world. Some external 3D authoring tools use coordinate systems where a different axis points up. Specify [`true`](../../../Swift/true.md) for this key to automatically transform all scene elements loaded from the file based on the [`SCNSceneSourceAssetUpAxisKey`](../../scnscenesourceassetupaxiskey.md) value stored in the file.

This option has no effect for assets compressed by Xcode. Instead, use Xcode itself to transform coordinate spaces when compressing the assets.

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
- [static let convertUnitsToMeters: SCNSceneSource.LoadingOption](./convertunitstometers.md)
  An option for whether to automatically scale the scene’s contents.
- [static let createNormalsIfAbsent: SCNSceneSource.LoadingOption](./createnormalsifabsent.md)
  An option for automatically generating surface normals if they are absent when loading geometry.
- [static let flattenScene: SCNSceneSource.LoadingOption](./flattenscene.md)
  An option for automatically merging portions of a scene graph during loading.
- [static let overrideAssetURLs: SCNSceneSource.LoadingOption](./overrideasseturls.md)
  An option to attempt loading external resources using their URLs as specified in a scene file.
- [static let preserveOriginalTopology: SCNSceneSource.LoadingOption](./preserveoriginaltopology.md)
- [static let strictConformance: SCNSceneSource.LoadingOption](./strictconformance.md)
  An option to interpret scene files exactly as specified by the scene file format.
- [static let useSafeMode: SCNSceneSource.LoadingOption](./usesafemode.md)
  An option to limit filesystem and network access for external resources referenced by a scene file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/converttoyup)*
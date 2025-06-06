# convertToYUp

**Framework**: SceneKit  
**Kind**: property

An option for whether to transform assets loaded from the scene file for use in a coordinate system where the y-axis points up.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let convertToYUp: SCNSceneSource.LoadingOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

SceneKit’s physics simulation works best when the y-axis of scene coordinate space corresponds to the “up” direction of the physics world. Some external 3D authoring tools use coordinate systems where a different axis points up. Specify [`true`](https://developer.apple.com/documentation/swift/true) for this key to automatically transform all scene elements loaded from the file based on the [`SCNSceneSourceAssetUpAxisKey`](scnscenesourceassetupaxiskey.md) value stored in the file.

This option has no effect for assets compressed by Xcode. Instead, use Xcode itself to transform coordinate spaces when compressing the assets.

## See Also

- [static let animationImportPolicy: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/animationimportpolicy.md)
  An option for controlling the playback of animations in a scene file.
- [SCNSceneSource.AnimationImportPolicy](scnscenesource/animationimportpolicy.md)
  Options for playing animations loaded from a scene file, used with the [`animationImportPolicy`](scnscenesource/loadingoption/animationimportpolicy.md) key in options dictionaries.
- [static let assetDirectoryURLs: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/assetdirectoryurls.md)
  Locations to use for resolving relative URLs to external resources.
- [static let checkConsistency: SCNSceneSource.LoadingOption](scnscenesource/loadingoption/checkconsistency.md)
  An option to validate scene files while loading.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption/converttoyup)*
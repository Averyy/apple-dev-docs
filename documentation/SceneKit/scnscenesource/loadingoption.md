# SCNSceneSource.LoadingOption

**Framework**: SceneKit  
**Kind**: struct

Options for creating scene sources and loading the scenes they contain.

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
struct LoadingOption
```

## Topics

### Type Properties
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
### Initializers
- [init(rawValue: String)](scnscenesource/loadingoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Scene Source Properties](scene-source-properties.md)
  The metadata properties associated with a scene file, used by the [`property(forKey:)`](scnscenesource/property(forkey:).md) method.
- [Contributor Keys](contributor-keys.md)
  Metadata identifying the user and authoring tool that created a scene file, used with the [`SCNSceneSourceAssetContributorsKey`](scnscenesourceassetcontributorskey.md) key.
- [Unit Dictionary Keys](unit-dictionary-keys.md)
  Metadata describing the unit of measurement used in a scene file, used with the [`SCNSceneSourceAssetUnitKey`](scnscenesourceassetunitkey.md) key.
- [Scene Loading Error Keys](scene-loading-error-keys.md)
- [Scene File Consistency Error Keys](scene-file-consistency-error-keys.md)
  Keys identifying errors found during a scene-file-format consistency check.
- [Scene File Consistency Check Error Codes](1573761-scene-file-consistency-check-err.md)
  Error codes that identify errors found during a scene-file-format consistency check.
- [typealias SCNSceneSourceStatusHandler](scnscenesourcestatushandler.md)
  The signature for the block that SceneKit calls periodically to report progress while loading a scene.
- [enum SCNSceneSourceStatus](scnscenesourcestatus.md)
  Constants identifying phases of SceneKit’s scene loading process, used in a [`SCNSceneSourceStatusHandler`](scnscenesourcestatushandler.md) block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/loadingoption)*
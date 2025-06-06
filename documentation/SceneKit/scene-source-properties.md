# Scene Source Properties

**Framework**: SceneKit

The metadata properties associated with a scene file, used by the [`property(forKey:)`](scnscenesource/property(forkey:).md) method.

## Topics

### Constants
- [let SCNSceneSourceAssetContributorsKey: String](scnscenesourceassetcontributorskey.md)
  The file contributors.
- [let SCNSceneSourceAssetCreatedDateKey: String](scnscenesourceassetcreateddatekey.md)
- [let SCNSceneSourceAssetModifiedDateKey: String](scnscenesourceassetmodifieddatekey.md)
- [let SCNSceneSourceAssetUpAxisKey: String](scnscenesourceassetupaxiskey.md)
- [let SCNSceneSourceAssetUnitKey: String](scnscenesourceassetunitkey.md)

## See Also

- [SCNSceneSource.LoadingOption](scnscenesource/loadingoption.md)
  Options for creating scene sources and loading the scenes they contain.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scene-source-properties)*
# Contributor Keys

**Framework**: SceneKit

Metadata identifying the user and authoring tool that created a scene file, used with the [`SCNSceneSourceAssetContributorsKey`](scnscenesourceassetcontributorskey.md) key.

#### Overview

Authoring tools that generate scene files may include metadata identifying the name and version of the authoring software and the name of the user who created the file. The values for these keys are [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects.

## Topics

### Constants
- [let SCNSceneSourceAssetAuthoringToolKey: String](scnscenesourceassetauthoringtoolkey.md)
  The authoring tool that created the scene file.
- [let SCNSceneSourceAssetAuthorKey: String](scnscenesourceassetauthorkey.md)
  The author of the scene file.

## See Also

- [SCNSceneSource.LoadingOption](scnscenesource/loadingoption.md)
  Options for creating scene sources and loading the scenes they contain.
- [Scene Source Properties](scene-source-properties.md)
  The metadata properties associated with a scene file, used by the [`property(forKey:)`](scnscenesource/property(forkey:).md) method.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/contributor-keys)*
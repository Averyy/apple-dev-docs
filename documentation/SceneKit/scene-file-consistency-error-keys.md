# Scene File Consistency Error Keys

**Framework**: SceneKit

Keys identifying errors found during a scene-file-format consistency check.

#### Overview

If you specify [`true`](https://developer.apple.com/documentation/Swift/true) for the [`checkConsistency`](scnscenesource/loadingoption/checkconsistency.md) when creating or loading from a scene source, SceneKit verifies the scene file against the specification for its file format. SceneKit reports any format verification issues that occur as an array of dictionaries, identified by the in the [`SCNDetailedErrorsKey`](scndetailederrorskey.md) key in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object. Each item in the array is a dictionary containing one or more of the keys listed above.

These keys and their values provide details about the location of the error in the scene file. Other properties of the returned [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object describe the nature of the validation error.

## Topics

### Constants
- [let SCNConsistencyElementIDErrorKey: String](scnconsistencyelementiderrorkey.md)
  The identifier of the scene file element where the error occurred.
- [let SCNConsistencyElementTypeErrorKey: String](scnconsistencyelementtypeerrorkey.md)
  The type of scene file element in which the error occurred.
- [let SCNConsistencyLineNumberErrorKey: String](scnconsistencylinenumbererrorkey.md)
  The line number in the scene file in which the error occurred.

## See Also

- [SCNSceneSource.LoadingOption](scnscenesource/loadingoption.md)
  Options for creating scene sources and loading the scenes they contain.
- [Scene Source Properties](scene-source-properties.md)
  The metadata properties associated with a scene file, used by the [`property(forKey:)`](scnscenesource/property(forkey:).md) method.
- [Contributor Keys](contributor-keys.md)
  Metadata identifying the user and authoring tool that created a scene file, used with the [`SCNSceneSourceAssetContributorsKey`](scnscenesourceassetcontributorskey.md) key.
- [Unit Dictionary Keys](unit-dictionary-keys.md)
  Metadata describing the unit of measurement used in a scene file, used with the [`SCNSceneSourceAssetUnitKey`](scnscenesourceassetunitkey.md) key.
- [Scene Loading Error Keys](scene-loading-error-keys.md)
- [Scene File Consistency Check Error Codes](1573761-scene-file-consistency-check-err.md)
  Error codes that identify errors found during a scene-file-format consistency check.
- [typealias SCNSceneSourceStatusHandler](scnscenesourcestatushandler.md)
  The signature for the block that SceneKit calls periodically to report progress while loading a scene.
- [enum SCNSceneSourceStatus](scnscenesourcestatus.md)
  Constants identifying phases of SceneKit’s scene loading process, used in a [`SCNSceneSourceStatusHandler`](scnscenesourcestatushandler.md) block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scene-file-consistency-error-keys)*
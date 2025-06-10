# Scene File Consistency Check Error Codes

**Framework**: SceneKit

Error codes that identify errors found during a scene-file-format consistency check.

#### Overview

If you specify [`true`](https://developer.apple.com/documentation/swift/true) for the [`checkConsistency`](scnscenesource/loadingoption/checkconsistency.md) when creating or loading from a scene source, SceneKit verifies the scene file against the specification for its file format. SceneKit reports any format verification issues in an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object whose [`code`](https://developer.apple.com/documentation/Foundation/NSError/code) property is one of these values.

For more details about the location and nature of any format validation errors, see the [`SCNDetailedErrorsKey`](scndetailederrorskey.md) key in the error’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary, and the keys listed in [`Scene File Consistency Error Keys`](scene-file-consistency-error-keys.md).

## Topics

### Constants
- [var SCNConsistencyInvalidURIError: Int](scnconsistencyinvalidurierror.md)
  The scene file contains an invalid URI (or URL).
- [var SCNConsistencyInvalidCountError: Int](scnconsistencyinvalidcounterror.md)
  The scene file contains an invalid number of scenes.
- [var SCNConsistencyInvalidArgumentError: Int](scnconsistencyinvalidargumenterror.md)
  An element in the scene file contains an invalid option for one of its attributes.
- [var SCNConsistencyMissingElementError: Int](scnconsistencymissingelementerror.md)
  A required element in the scene file is missing.
- [var SCNConsistencyMissingAttributeError: Int](scnconsistencymissingattributeerror.md)
  An element in the scene file is missing a required attribute.
- [var SCNConsistencyXMLSchemaValidationError: Int](scnconsistencyxmlschemavalidationerror.md)
  The format of the scene file does not match its XML schema definition.

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
- [Scene File Consistency Error Keys](scene-file-consistency-error-keys.md)
  Keys identifying errors found during a scene-file-format consistency check.
- [typealias SCNSceneSourceStatusHandler](scnscenesourcestatushandler.md)
  The signature for the block that SceneKit calls periodically to report progress while loading a scene.
- [enum SCNSceneSourceStatus](scnscenesourcestatus.md)
  Constants identifying phases of SceneKit’s scene loading process, used in a [`SCNSceneSourceStatusHandler`](scnscenesourcestatushandler.md) block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/1573761-scene-file-consistency-check-err)*
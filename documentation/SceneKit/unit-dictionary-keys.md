# Unit Dictionary Keys

**Framework**: SceneKit

Metadata describing the unit of measurement used in a scene file, used with the [`SCNSceneSourceAssetUnitKey`](scnscenesourceassetunitkey.md) key.

#### Overview

By default, units of measurement for SceneKit are entirely arbitrary. A geometry’s vertex data is defined in whatever unit system and coordinate space is convenient for its author. The nodes in a scene each define their own space as is convenient for organizing the scene’s contents, and the camera that views a scene and the renderer that draws it determine the correspondence between the scene’s world and the pixels on a display.

Nevertheless, it can be useful for authors of 3D assets to establish a unit scale for the art they create. A scene file can identify the intended unit of measure for the world space their contents are defined in. If you load assets from multiple sources and combine them in a single scene, you can use the units specified in each source to determine how to scale each asset in the combined scene. When working with units from a scene file, the arbitrary unit of distance that SceneKit’s world space corresponds to the meter defined in the International System of Units (SI).

For example, one scene file might contain geometry representing a vehicle, having no designated unit but designed on a scale where one unit equals one meter. Another scene file might contain geometry representing a person, with a designated unit of US—the unit dictionary for the scene file contains the string `inch` for the [`SCNSceneSourceAssetUnitNameKey`](scnscenesourceassetunitnamekey.md) key, and the number `0.0254` for the [`SCNSceneSourceAssetUnitMeterKey`](scnscenesourceassetunitmeterkey.md) key. To place these objects together in the same scene at appropriate sizes, set the [`scale`](scnnode/scale.md) property of the node containing the person geometry to `0.0254`.

## Topics

### Constants
- [let SCNSceneSourceAssetUnitNameKey: String](scnscenesourceassetunitnamekey.md)
  The name of the unit used in the scene file.
- [let SCNSceneSourceAssetUnitMeterKey: String](scnscenesourceassetunitmeterkey.md)
  The conversion factor from the unit used in the scene file to the SI meter.

## See Also

- [SCNSceneSource.LoadingOption](scnscenesource/loadingoption.md)
  Options for creating scene sources and loading the scenes they contain.
- [Scene Source Properties](scene-source-properties.md)
  The metadata properties associated with a scene file, used by the [`property(forKey:)`](scnscenesource/property(forkey:).md) method.
- [Contributor Keys](contributor-keys.md)
  Metadata identifying the user and authoring tool that created a scene file, used with the [`SCNSceneSourceAssetContributorsKey`](scnscenesourceassetcontributorskey.md) key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/unit-dictionary-keys)*
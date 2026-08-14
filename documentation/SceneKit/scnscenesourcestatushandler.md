# SCNSceneSourceStatusHandler

**Framework**: SceneKit  
**Kind**: typealias

The signature for the block that SceneKit calls periodically to report progress while loading a scene.

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
typealias SCNSceneSourceStatusHandler = (Float, SCNSceneSourceStatus, (any Error)?, UnsafeMutablePointer<ObjCBool>) -> Void
```

#### Discussion

You provide a block with this signature when using the [`scene(options:statusHandler:)`](scnscenesource/scene(options:statushandler:).md) method.

The block takes four parameters:

- **totalProgress**: A floating-point number between `0.0` and `1.0` indicating the overall progress of loading the scene. A value of `0.0` indicates that the loading process has just begun, and a value of `1.0` indicates that the process has completed.
- **status**: A constant identifying one of the distinct phases of SceneKit’s loading procedure. See [`SCNSceneSourceStatus`](scnscenesourcestatus.md) for possible values.
- **error**: An error object describing any error that has occurred during scene loading, or `nil` if no errors has been encountered.
- **stopLoading**: A reference to a Boolean value. Set `*stop` to [`true`](https://developer.apple.com/documentation/swift/true) within the block to abort further processing of the scene source’s contents.

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
- [Scene File Consistency Check Error Codes](1573761-scene-file-consistency-check-err.md)
  Error codes that identify errors found during a scene-file-format consistency check.
- [enum SCNSceneSourceStatus](scnscenesourcestatus.md)
  Constants identifying phases of SceneKit’s scene loading process, used in a [`SCNSceneSourceStatusHandler`](scnscenesourcestatushandler.md) block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesourcestatushandler)*
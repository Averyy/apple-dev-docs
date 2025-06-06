# SCNSceneSource

**Framework**: SceneKit  
**Kind**: class

An object that manages the data-reading tasks associated with loading scene contents from a file or data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNSceneSource
```

## Mentions

- [Animating SceneKit Content](animating-scenekit-content.md)

#### Overview

You can also use a scene source to examine the contents of a scene file or to selectively extract certain elements of a scene without keeping the entire scene and all the assets it contains.

SceneKit can read scene contents from a file in a supported format, or from an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object holding the contents of such a file. Supported formats include the following:

| Format | Filename Extension | Supported in |
| --- | --- | --- |
| Digital Asset Exchange | `.dae` | macOS 10.8 and later |
| Alembic | `.abc` | macOS 10.10 and later |
| SceneKit compressed scene | `.dae` or `.abc` | macOS 10.10 and later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) iOS 8.0 and later |
| SceneKit archive | `.scn` | macOS 10.10 and later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) iOS 8.0 and later |

When you include a scene file in DAE or Alembic format in your Xcode project, Xcode automatically converts the file to SceneKit’s compressed scene format for use in the built app. The compressed file retains its original `.dae` or `.abc` extension.

The [`SCNSceneSource`](scnscenesource.md) class can also load SceneKit archive files, which you create in the Xcode scene editor or programmatically by using the [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) class to serialize an [`SCNScene`](scnscene.md) object and the scene graph it contains.

> **Note**:  For best results, place scene files that ship in your app bundle in a folder with the `.scnassets` extension, and place image files referenced as textures from those scenes in an Asset Catalog. Xcode then optimizes the scene and texture resources for best performance on each target device, and prepares your texture resources for delivery features such as App Thinning and On-Demand Resources.

 For best results, place scene files that ship in your app bundle in a folder with the `.scnassets` extension, and place image files referenced as textures from those scenes in an Asset Catalog. Xcode then optimizes the scene and texture resources for best performance on each target device, and prepares your texture resources for delivery features such as App Thinning and On-Demand Resources.

## Topics

### Creating a Scene Source
- [init?(url: URL, options: [SCNSceneSource.LoadingOption : Any]?)](scnscenesource/init(url:options:).md)
  Initializes a scene source for reading the scene graph from a specified file.
- [init?(data: Data, options: [SCNSceneSource.LoadingOption : Any]?)](scnscenesource/init(data:options:).md)
  Initializes a scene source for reading the scene graph contained in an `NSData` object.
### Loading a Complete Scene
- [func scene(options: [SCNSceneSource.LoadingOption : Any]?, statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene?](scnscenesource/scene(options:statushandler:).md)
  Loads the entire scene graph from the scene source and calls the specified block to provide progress information.
- [func scene(options: [SCNSceneSource.LoadingOption : Any]?) throws -> SCNScene](scnscenesource/scene(options:).md)
  Instantiates a scene from the scene source with the specified options.
### Loading and Inspecting Scene Elements
- [func identifiersOfEntries(withClass: AnyClass) -> [String]](scnscenesource/identifiersofentries(withclass:).md)
  Returns the identifiers for all objects in the scene source of the specified class.
- [func entryWithIdentifier<T>(String, withClass: T.Type) -> T?](scnscenesource/entrywithidentifier(_:withclass:).md)
  Loads and returns a specific object in the scene source.
- [func entries(passingTest: (Any, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [Any]](scnscenesource/entries(passingtest:).md)
  Loads and returns all objects in the scene source that pass the test in a given block.
### Getting Information about the Scene
- [var url: URL?](scnscenesource/url.md)
  The URL identifying the file from which the scene source was created.
- [var data: Data?](scnscenesource/data.md)
  The data object from which the scene source loads scene content.
- [func property(forKey: String) -> Any?](scnscenesource/property(forkey:).md)
  Returns metadata about the scene.
### Constants
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
- [typealias SCNSceneSourceStatusHandler](scnscenesourcestatushandler.md)
  The signature for the block that SceneKit calls periodically to report progress while loading a scene.
- [enum SCNSceneSourceStatus](scnscenesourcestatus.md)
  Constants identifying phases of SceneKit’s scene loading process, used in a [`SCNSceneSourceStatusHandler`](scnscenesourcestatushandler.md) block.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource)*
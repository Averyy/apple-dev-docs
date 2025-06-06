# scene(options:statusHandler:)

**Framework**: SceneKit  
**Kind**: method

Loads the entire scene graph from the scene source and calls the specified block to provide progress information.

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
func scene(options: [SCNSceneSource.LoadingOption : Any]? = nil, statusHandler: SCNSceneSourceStatusHandler? = nil) -> SCNScene?
```

#### Return Value

An [`SCNScene`](scnscene.md) object containing the entire scene graph from the scene source, or `nil` if loading was not successful.

#### Discussion

Use this method if you need to monitor progress while loading a scene from the scene source. For simpler scene loading, use the [`scene(options:)`](scnscenesource/scene(options:).md) method or the [`SCNScene`](scnscene.md) method [`init(url:options:)`](scnscene/init(url:options:).md).

A scene source can contain objects that are not part of its scene graph. To obtain these objects, you must load them individually with the the [`entryWithIdentifier:withClass:`](scnscenesource/entrywithidentifier:withclass:.md) or [`entries(passingTest:)`](scnscenesource/entries(passingtest:).md) method. For example, a scene file containing a game character could include several animations for the character geometry (such as running, jumping, and standing idle). Because you typically do not apply multiple animations at once, the scene file contains these animations without their being attached to the character geometry.

## Parameters

- `options`: A dictionary containing options that affect scene loading. See   for available keys and values. Pass   to use default options.
- `statusHandler`: An   block. SceneKit calls this block periodically to report progress while loading the scene.

## See Also

- [func scene(options: [SCNSceneSource.LoadingOption : Any]?) throws -> SCNScene](scnscenesource/scene(options:).md)
  Instantiates a scene from the scene source with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/scene(options:statushandler:))*
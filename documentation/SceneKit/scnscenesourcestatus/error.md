# SCNSceneSourceStatus.error

**Framework**: SceneKit  
**Kind**: case

An error occurred when SceneKit attempted to load the scene.

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
case error
```

#### Discussion

If the `status` parameter of a [`SCNSceneSourceStatusHandler`](scnscenesourcestatushandler.md) block has this value, see the block’s `error` parameter for information about the nature and location of the error. When SceneKit encounters an error during scene loading, it calls the handler block with this status, then after the block completes, the [`scene(options:statusHandler:)`](scnscenesource/scene(options:statushandler:).md) method returns `nil`.

## See Also

- [SCNSceneSourceStatus.parsing](scnscenesourcestatus/parsing.md)
  SceneKit has begun deserializing the source file.
- [SCNSceneSourceStatus.validating](scnscenesourcestatus/validating.md)
  SceneKit has begun validating the scene file’s format.
- [SCNSceneSourceStatus.processing](scnscenesourcestatus/processing.md)
  SceneKit has begun generating scene graph objects from the scene file’s contents.
- [SCNSceneSourceStatus.complete](scnscenesourcestatus/complete.md)
  SceneKit has successfully finished loading the scene file’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesourcestatus/error)*
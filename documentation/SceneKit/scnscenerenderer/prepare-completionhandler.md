# prepare(_:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Prepares the specified SceneKit objects for rendering, using a background thread.

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
func prepare(_ objects: [Any]) async -> Bool
```

#### Discussion

By default, SceneKit lazily loads resources onto the GPU for rendering. This approach uses memory and GPU bandwidth efficiently, but can lead to stutters in an otherwise smooth frame rate when you add large amounts of new content to an animated scene. To avoid such issues, use this method to prepare content for drawing before adding it to the scene. SceneKit uses a secondary thread to prepare content asynchronously.

SceneKit prepares all content associated with the objects you provide. If you provide an [`SCNMaterial`](scnmaterial.md) object, SceneKit loads any texture images assigned to its material properties. If you provide an [`SCNGeometry`](scngeometry.md) object, SceneKit loads all materials attached to the geometry, as well as its vertex data. If you provide an [`SCNNode`](scnnode.md) or [`SCNScene`](scnscene.md) object, SceneKit loads all geometries and materials associated with the node and all its child nodes, or with the entire node hierarchy of the scene.

You can observe the progress of this operation with the [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) class. For details, see [`Progress`](https://developer.apple.com/documentation/Foundation/Progress).

## Parameters

- `objects`: An array of containing one or more  ,  ,  , or   instances.
- `completionHandler`: The block takes the following parameter:

## See Also

- [func prepare(Any, shouldAbortBlock: (() -> Bool)?) -> Bool](scnscenerenderer/prepare(_:shouldabortblock:).md)
  Prepares a SceneKit object for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/prepare(_:completionhandler:))*
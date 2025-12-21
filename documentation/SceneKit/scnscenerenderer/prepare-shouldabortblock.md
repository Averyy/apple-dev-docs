# prepare(_:shouldAbortBlock:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Prepares a SceneKit object for rendering.

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
func prepare(_ object: Any, shouldAbortBlock block: (() -> Bool)? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the object was successfully prepared for rendering, or [`false`](https://developer.apple.com/documentation/Swift/false) if preparation was canceled.

#### Discussion

By default, SceneKit lazily loads resources onto the GPU for rendering. This approach uses memory and GPU bandwidth efficiently, but can lead to stutters in an otherwise smooth frame rate when you add large amounts of new content to an animated scene. To avoid such issues, use this method to prepare content for drawing before adding it to the scene. You can call this method on a secondary thread to prepare content asynchronously.

SceneKit prepares all content associated with the `object` parameter you provide. If you provide an [`SCNMaterial`](scnmaterial.md) object, SceneKit loads any texture images assigned to its material properties. If you provide an [`SCNGeometry`](scngeometry.md) object, SceneKit loads all materials attached to the geometry, as well as its vertex data. If you provide an [`SCNNode`](scnnode.md) or [`SCNScene`](scnscene.md) object, SceneKit loads all geometries and materials associated with the node and all its child nodes, or with the entire node hierarchy of the scene.

You can use the `block` parameter to cancel preparation if content is no longer needed. For example, in a game you might use this method to preload areas of the game world the player is soon to enter, but if the player character dies before entering those areas, you can return [`true`](https://developer.apple.com/documentation/Swift/true) from the block to cancel preloading.

You can observe the progress of this operation with the [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) class. For details, see [`Progress`](https://developer.apple.com/documentation/Foundation/Progress).

## Parameters

- `object`: An  ,  ,  , or   instance.
- `block`: Pass   for this parameter if you do not need an opportunity to cancel preparing the object.

## See Also

- [func prepare([Any], completionHandler: ((Bool) -> Void)?)](scnscenerenderer/prepare(_:completionhandler:).md)
  Prepares the specified SceneKit objects for rendering, using a background thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/prepare(_:shouldabortblock:))*
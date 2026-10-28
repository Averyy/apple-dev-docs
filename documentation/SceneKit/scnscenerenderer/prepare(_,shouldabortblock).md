# prepare(_:shouldAbortBlock:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepares a SceneKit object for rendering.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func prepare(_ object: Any, shouldAbortBlock block: (() -> Bool)? = nil) -> Bool
```

```objc
- (BOOL) prepareObject:(id) object shouldAbortBlock:(BOOL (^)()) block;
```

## Return Value

[`true`](../../Swift/true.md) if the object was successfully prepared for rendering, or [`false`](../../Swift/false.md) if preparation was canceled.

## Discussion

By default, SceneKit lazily loads resources onto the GPU for rendering. This approach uses memory and GPU bandwidth efficiently, but can lead to stutters in an otherwise smooth frame rate when you add large amounts of new content to an animated scene. To avoid such issues, use this method to prepare content for drawing before adding it to the scene. You can call this method on a secondary thread to prepare content asynchronously.

SceneKit prepares all content associated with the `object` parameter you provide. If you provide an [`SCNMaterial`](../scnmaterial.md) object, SceneKit loads any texture images assigned to its material properties. If you provide an [`SCNGeometry`](../scngeometry.md) object, SceneKit loads all materials attached to the geometry, as well as its vertex data. If you provide an [`SCNNode`](../scnnode.md) or [`SCNScene`](../scnscene.md) object, SceneKit loads all geometries and materials associated with the node and all its child nodes, or with the entire node hierarchy of the scene.

You can use the `block` parameter to cancel preparation if content is no longer needed. For example, in a game you might use this method to preload areas of the game world the player is soon to enter, but if the player character dies before entering those areas, you can return [`true`](../../Swift/true.md) from the block to cancel preloading.

You can observe the progress of this operation with the [`Progress`](../../Foundation/progress.md) class. For details, see [`Progress`](../../Foundation/progress.md).

## Parameters

- `object`: An [`SCNScene`](../scnscene.md), [`SCNNode`](../scnnode.md), [`SCNGeometry`](../scngeometry.md), or [`SCNMaterial`](../scnmaterial.md) instance.
- `block`: A block that SceneKit calls periodically while preparing the object. The block takes no parameters.

  Your block should return [`false`](../../Swift/false.md) to tell SceneKit to continue preparing the object, or [`true`](../../Swift/true.md) to cancel preparation.

  Pass `nil` for this parameter if you do not need an opportunity to cancel preparing the object.

## See Also

### Preloading Renderer Resources
- [func prepare([Any], completionHandler: ((Bool) -> Void)?)](./prepare%28_,completionhandler%29.md)
  Prepares the specified SceneKit objects for rendering, using a background thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/prepare(_:shouldabortblock:))*
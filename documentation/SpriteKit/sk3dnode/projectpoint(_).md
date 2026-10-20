# projectPoint(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Projects a point from the 3D world coordinate system of the SceneKit scene to the 2D viewport coordinate system of the SpriteKit node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func projectPoint(_ point: vector_float3) -> vector_float3
```

```objc
- (vector_float3) projectPoint:(vector_float3) point;
```

#### Return Value

The corresponding point in the SpriteKit node’s coordinate system.

#### Discussion

The z-coordinate of the returned point describes the depth of the projected point relative to the near and far clipping planes of the viewing frustum (defined by the [`pointOfView`](./pointofview.md) property). Projecting a point on the near clipping plane returns a point whose z-coordinate is `0.0`; projecting a point on the far clipping plane returns a point whose z-coordinate is `1.0`.

The following Swift code illustrates how you might convert the position of a SceneKit node, `sphereNode`, in 3D space to the 2D coordinates of a SpriteKit [`SK3DNode`](../sk3dnode.md), `node`. The code assumes that `sphereNode` is the first child node of the SceneKit scene’s [`rootNode`](../../SceneKit/scnscene/rootnode.md).

```swift
if let sphereNode = node.scnScene?.rootNode.childNodes.first { 
    let location = node.projectPoint(vector_float3(Float(sphereNode.position.x),
                                                   Float(sphereNode.position.y),
                                                   Float(sphereNode.position.z)))
}
```

## Parameters

- `point`: A point in the world coordinate system of the Scene Kit scene.

## See Also

### Projecting Points and Performing Hit-Testing
- [func hitTest(CGPoint, options: [String : Any]?) -> [SCNHitTestResult]](./hittest%28_,options%29.md)
  Searches the Scene Kit scene for objects corresponding to a point in the rendered image.
- [func unprojectPoint(vector_float3) -> vector_float3](./unprojectpoint%28_%29.md)
  Unprojects a point from the SpriteKit node’s 2D viewport coordinate system to the 3D world coordinate system of the SceneKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/projectpoint(_:))*
# worldTransform

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The world transform applied to the node.

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
var worldTransform: SCNMatrix4 { get }
```

```objc
@property (nonatomic, readonly) SCNMatrix4 worldTransform;
```

## Discussion

A world transform is the node’s coordinate space transform relative to the scene’s coordinate space. This transform is the concatenation of the node’s [`transform`](./transform.md) property with that of its parent node, the parent’s parent, and so on up to the [`rootNode`](../scnscene/rootnode.md) object of the scene.

> **Note**:  In macOS 10.13, iOS 11, tvOS 11, or watchOS 4 (and later), you can set this value with the [`setWorldTransform(_:)`](./setworldtransform%28_%29.md) method.

## See Also

### Related Documentation
- [var simdWorldTransform: simd_float4x4](./simdworldtransform.md)
  The world transform applied to the node.
- [var parent: SCNNode?](./parent.md)
  The node’s parent in the scene graph hierarchy.
### Managing Transforms in World Space (SceneKit Types)
- [func setWorldTransform(SCNMatrix4)](./setworldtransform%28_%29.md)
  Sets the world transform applied to the node.
- [var worldOrientation: SCNQuaternion](./worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var worldPosition: SCNVector3](./worldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldtransform)*
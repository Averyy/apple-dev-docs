# worldPosition

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The node’s position relative to the scene’s world coordinate space.

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
var worldPosition: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 worldPosition;
```

## Discussion

This vector isolates the translational aspect of the node’s [`worldTransform`](./worldtransform.md) matrix, which in turn is the conversion of the node’s [`transform`](./transform.md) from local space to the scene’s world coordinate space. That is, it expresses the x, y, and z offsets of the node’s position from that of the scene’s [`rootNode`](../scnscene/rootnode.md), and is equivalent to reading the node’s [`position`](./position.md) vector and converting it to world space with the [`convertPosition(_:from:)`](./convertposition%28_,from%29.md) or [`convertPosition(_:to:)`](./convertposition%28_,to%29.md) method.

## See Also

### Related Documentation
- [var simdWorldPosition: simd_float3](./simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.
### Managing Transforms in World Space (SceneKit Types)
- [var worldTransform: SCNMatrix4](./worldtransform.md)
  The world transform applied to the node.
- [func setWorldTransform(SCNMatrix4)](./setworldtransform%28_%29.md)
  Sets the world transform applied to the node.
- [var worldOrientation: SCNQuaternion](./worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldposition)*
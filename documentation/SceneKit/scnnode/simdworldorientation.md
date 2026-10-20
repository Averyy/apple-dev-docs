# simdWorldOrientation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The node’s orientation relative to the scene’s world coordinate space.

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
var simdWorldOrientation: simd_quatf { get set }
```

```objc
@property (nonatomic) simd_quatf simdWorldOrientation;
```

#### Discussion

This quaternion isolates the rotational aspect of the node’s [`simdWorldTransform`](./simdworldtransform.md) matrix, which in turn is the conversion of the node’s [`simdTransform`](./simdtransform.md) from local space to the scene’s world coordinate space. That is, it expresses the difference in axis and angle of rotation between the node and the scene’s [`rootNode`](../scnscene/rootnode.md).

## See Also

### Related Documentation
- [var worldOrientation: SCNQuaternion](./worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
### Managing Transforms in World Space
- [var simdWorldTransform: simd_float4x4](./simdworldtransform.md)
  The world transform applied to the node.
- [var simdWorldPosition: simd_float3](./simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldorientation)*
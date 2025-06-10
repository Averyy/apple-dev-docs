# simdConvertVector(_:from:)

**Framework**: SceneKit  
**Kind**: method

Converts a direction vector to the node’s local coordinate space from that of another node.

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
func simdConvertVector(_ vector: simd_float3, from node: SCNNode?) -> simd_float3
```

#### Return Value

A direction vector in the node’s local coordinate space.

#### Discussion

Unlike the [`simdConvertPosition(_:from:)`](scnnode/simdconvertposition(_:from:).md) method, this method ignores the translational aspect of both nodes’ transforms. As such, this method is more appropriate for use with vectors that represent only directional information, such as velocity or facing.

## Parameters

- `vector`: A direction vector in the local coordinate space defined by the other node.
- `node`: Another node in the same scene graph as the node, or   to convert from the scene’s world coordinate space.

## See Also

- [func convertVector(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func simdConvertPosition(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func simdConvertPosition(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func simdConvertTransform(simd_float4x4, from: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func simdConvertVector(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdconvertvector(_:from:))*
# simdConvertPosition(_:to:)

**Framework**: SceneKit  
**Kind**: method

Converts a position from the node’s local coordinate space to that of another node.

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
func simdConvertPosition(_ position: simd_float3, to node: SCNNode?) -> simd_float3
```

#### Return Value

A position in the local coordinate space defined by the other node.

## Parameters

- `position`: A position in the node’s local coordinate space.
- `node`: Another node in the same scene graph as the node, or   to convert to the scene’s world coordinate space.

## See Also

- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func simdConvertPosition(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func simdConvertTransform(simd_float4x4, from: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func simdConvertVector(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func simdConvertVector(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdconvertposition(_:to:))*
# simdConvertTransform(_:from:)

**Framework**: SceneKit  
**Kind**: method

Converts a transform to the node’s local coordinate space from that of another node.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func simdConvertTransform(_ transform: simd_float4x4, from node: SCNNode?) -> simd_float4x4
```

#### Return Value

A transform relative to the node’s coordinate space.

## Parameters

- `transform`: A transform relative to the local coordinate space defined by the other node.
- `node`: Another node in the same scene graph as the node, or   to convert from the scene’s world coordinate space.

## See Also

- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func simdConvertPosition(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func simdConvertPosition(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func simdConvertVector(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func simdConvertVector(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdconverttransform(_:from:))*
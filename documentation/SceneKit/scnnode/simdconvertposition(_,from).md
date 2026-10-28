# simdConvertPosition(_:from:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Converts a position to the node’s local coordinate space from that of another node.

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
func simdConvertPosition(_ position: simd_float3, from node: SCNNode?) -> simd_float3
```

```objc
- (simd_float3) simdConvertPosition:(simd_float3) position fromNode:(SCNNode *) node;
```

## Return Value

A position in the node’s local coordinate space.

## Parameters

- `position`: A position in the local coordinate space defined by the other node.
- `node`: Another node in the same scene graph as the node, or `nil` to convert from the scene’s world coordinate space.

## See Also

### Related Documentation
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](./convertposition%28_,from%29.md)
  Converts a position to the node’s local coordinate space from that of another node.
### Converting Between Coordinate Spaces
- [func simdConvertPosition(simd_float3, to: SCNNode?) -> simd_float3](./simdconvertposition%28_,to%29.md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func simdConvertTransform(simd_float4x4, from: SCNNode?) -> simd_float4x4](./simdconverttransform%28_,from%29.md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](./simdconverttransform%28_,to%29.md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func simdConvertVector(simd_float3, from: SCNNode?) -> simd_float3](./simdconvertvector%28_,from%29.md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func simdConvertVector(simd_float3, to: SCNNode?) -> simd_float3](./simdconvertvector%28_,to%29.md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdconvertposition(_:from:))*
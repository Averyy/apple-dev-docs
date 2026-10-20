# convertVector(_:from:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Converts a direction vector to the node’s local coordinate space from that of another node.

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
func convertVector(_ vector: SCNVector3, from node: SCNNode?) -> SCNVector3
```

```objc
- (SCNVector3) convertVector:(SCNVector3) vector fromNode:(SCNNode *) node;
```

#### Return Value

A direction vector in the node’s local coordinate space.

#### Discussion

Unlike the [`convertPosition(_:from:)`](./convertposition%28_,from%29.md) method, this method ignores the translational aspect of both nodes’ transforms. As such, this method is more appropriate for use with vectors that represent only directional information, such as velocity or facing.

## Parameters

- `vector`: A direction vector in the local coordinate space defined by the other node.
- `node`: Another node in the same scene graph as the node, or `nil` to convert from the scene’s world coordinate space.

## See Also

### Related Documentation
- [func simdConvertVector(simd_float3, from: SCNNode?) -> simd_float3](./simdconvertvector%28_,from%29.md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
### Converting Between Coordinate Spaces (SceneKit Types)
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](./convertposition%28_,from%29.md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](./convertposition%28_,to%29.md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](./converttransform%28_,from%29.md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertTransform(SCNMatrix4, to: SCNNode?) -> SCNMatrix4](./converttransform%28_,to%29.md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](./convertvector%28_,to%29.md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/convertvector(_:from:))*
# convertTransform(_:to:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Converts a transform from the node’s local coordinate space to that of another node.

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
func convertTransform(_ transform: SCNMatrix4, to node: SCNNode?) -> SCNMatrix4
```

```objc
- (SCNMatrix4) convertTransform:(SCNMatrix4) transform toNode:(SCNNode *) node;
```

## Return Value

A transform relative to the local coordinate space defined by the other node.

## Parameters

- `transform`: A transform relative to the node’s coordinate space.
- `node`: Another node in the same scene graph as the node, or `nil` to convert to the scene’s world coordinate space.

## See Also

### Related Documentation
- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](./simdconverttransform%28_,to%29.md)
  Converts a transform from the node’s local coordinate space to that of another node.
### Converting Between Coordinate Spaces (SceneKit Types)
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](./convertposition%28_,from%29.md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](./convertposition%28_,to%29.md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](./converttransform%28_,from%29.md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, from: SCNNode?) -> SCNVector3](./convertvector%28_,from%29.md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](./convertvector%28_,to%29.md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/converttransform(_:to:))*
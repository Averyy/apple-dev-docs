# convertVector(_:from:)

**Framework**: SceneKit  
**Kind**: method

Converts a direction vector to the node’s local coordinate space from that of another node.

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
func convertVector(_ vector: SCNVector3, from node: SCNNode?) -> SCNVector3
```

#### Return Value

A direction vector in the node’s local coordinate space.

#### Discussion

Unlike the [`convertPosition(_:from:)`](scnnode/convertposition(_:from:).md) method, this method ignores the translational aspect of both nodes’ transforms. As such, this method is more appropriate for use with vectors that represent only directional information, such as velocity or facing.

## Parameters

- `vector`: A direction vector in the local coordinate space defined by the other node.
- `node`: Another node in the same scene graph as the node, or   to convert from the scene’s world coordinate space.

## See Also

- [func simdConvertVector(simd_float3, from: SCNNode?) -> simd_float3](scnnode/simdconvertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertTransform(SCNMatrix4, to: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/convertvector(_:from:))*
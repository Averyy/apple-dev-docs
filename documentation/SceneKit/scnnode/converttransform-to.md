# convertTransform(_:to:)

**Framework**: SceneKit  
**Kind**: method

Converts a transform from the node’s local coordinate space to that of another node.

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
func convertTransform(_ transform: SCNMatrix4, to node: SCNNode?) -> SCNMatrix4
```

#### Return Value

A transform relative to the local coordinate space defined by the other node.

## Parameters

- `transform`: A transform relative to the node’s coordinate space.
- `node`: Another node in the same scene graph as the node, or   to convert to the scene’s world coordinate space.

## See Also

- [func simdConvertTransform(simd_float4x4, to: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/converttransform(_:to:))*
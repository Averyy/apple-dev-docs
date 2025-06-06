# convertPosition(_:to:)

**Framework**: SceneKit  
**Kind**: method

Converts a position from the node’s local coordinate space to that of another node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func convertPosition(_ position: SCNVector3, to node: SCNNode?) -> SCNVector3
```

#### Return Value

A position in the local coordinate space defined by the other node.

## Parameters

- `position`: A position in the node’s local coordinate space.
- `node`: Another node in the same scene graph as the node, or   to convert to the scene’s world coordinate space.

## See Also

- [func simdConvertPosition(simd_float3, to: SCNNode?) -> simd_float3](scnnode/simdconvertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertTransform(SCNMatrix4, from: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertTransform(SCNMatrix4, to: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func convertVector(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/convertposition(_:to:))*
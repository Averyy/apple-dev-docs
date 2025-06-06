# convertTransform(_:from:)

**Framework**: SceneKit  
**Kind**: method

Converts a transform to the node’s local coordinate space from that of another node.

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
func convertTransform(_ transform: SCNMatrix4, from node: SCNNode?) -> SCNMatrix4
```

#### Return Value

A transform relative to the node’s coordinate space.

## Parameters

- `transform`: A transform relative to the local coordinate space defined by the other node.
- `node`: Another node in the same scene graph as the node, or   to convert from the scene’s world coordinate space.

## See Also

- [func simdConvertTransform(simd_float4x4, from: SCNNode?) -> simd_float4x4](scnnode/simdconverttransform(_:from:).md)
  Converts a transform to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertposition(_:from:).md)
  Converts a position to the node’s local coordinate space from that of another node.
- [func convertPosition(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertposition(_:to:).md)
  Converts a position from the node’s local coordinate space to that of another node.
- [func convertTransform(SCNMatrix4, to: SCNNode?) -> SCNMatrix4](scnnode/converttransform(_:to:).md)
  Converts a transform from the node’s local coordinate space to that of another node.
- [func convertVector(SCNVector3, from: SCNNode?) -> SCNVector3](scnnode/convertvector(_:from:).md)
  Converts a direction vector to the node’s local coordinate space from that of another node.
- [func convertVector(SCNVector3, to: SCNNode?) -> SCNVector3](scnnode/convertvector(_:to:).md)
  Converts a direction vector from the node’s local coordinate space to that of another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/converttransform(_:from:))*
# MeshJointInfluence

**Framework**: RealityKit  
**Kind**: struct

A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct MeshJointInfluence
```

#### Overview

A vertex may be influenced by one or more joints. The skinned position of that vertex is defined by a set of MeshJointInfluence values whose weights sum to 1. The skinned position is given by:

```swift
position = vertexPosition(transformedByJoint: influences[0].jointIndex) * influences[0].weight
         + vertexPosition(transformedByJoint: influences[1].jointIndex) * influences[1].weight
         + ...
```

The skinned position of a vertex is a linear combination of the vertex’s position transformed by each joint, with weights given by the MeshJointInfluence values.

To transform a vertex position by a joint, the initial vertex position is first transformed by the joint’s inverse bind pose matrix, then by the local-to-parent transform of the joint, and finally by the local-to-parent transform of each of the joint’s parents.

## Topics

### Initializers
- [init()](meshjointinfluence/init.md)
- [init(jointIndex: Int, weight: Float)](meshjointinfluence/init(jointindex:weight:).md)
### Instance Properties
- [var jointIndex: Int](meshjointinfluence/jointindex.md)
- [var weight: Float](meshjointinfluence/weight.md)

## See Also

- [struct MeshSkeletonCollection](meshskeletoncollection.md)
  An object that holds a collection of skeletons used by a mesh resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshjointinfluence)*
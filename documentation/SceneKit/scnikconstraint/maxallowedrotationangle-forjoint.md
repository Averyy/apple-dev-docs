# maxAllowedRotationAngle(forJoint:)

**Framework**: SceneKit  
**Kind**: method

Returns the rotation limit, in degrees, for the specified node.

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
func maxAllowedRotationAngle(forJoint node: SCNNode) -> CGFloat
```

#### Return Value

The maximum rotation, in degrees, that SceneKit applies to the specified node when evaluating the constraint.

#### Discussion

When SceneKit evaluates the IK constraint, it checks the target orientations of each node in the chain relative to their initial orientations (as of when the constraint was applied to a node). For each node in the chain, SceneKit limits the rotation (in any direction) between the initial and target orientations to the value returned by this method.

The default rotation limit for each joint is 180 degrees in either direction, allowing unconstrained rotation.

## Parameters

- `node`: A node affected by the constraint—either the node whose   property references the constraint or one of that node’s parent or ancestor nodes, up to the node specified by the constraint’s   property.

## See Also

- [var chainRootNode: SCNNode](scnikconstraint/chainrootnode.md)
  The parent node of the hierarchy affected by the constraint.
- [func setMaxAllowedRotationAngle(CGFloat, forJoint: SCNNode)](scnikconstraint/setmaxallowedrotationangle(_:forjoint:).md)
  Sets the rotation limit, in degrees, for the specified node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnikconstraint/maxallowedrotationangle(forjoint:))*
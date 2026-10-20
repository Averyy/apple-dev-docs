# setMaxAllowedRotationAngle(_:forJoint:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Sets the rotation limit, in degrees, for the specified node.

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
func setMaxAllowedRotationAngle(_ angle: CGFloat, forJoint node: SCNNode)
```

```objc
- (void) setMaxAllowedRotationAngle:(CGFloat) angle forJoint:(SCNNode *) node;
```

#### Discussion

When SceneKit evaluates the IK constraint, it checks the target orientations of each node in the chain relative to their initial orientations (as of when the constraint was applied to a node). For each node in the chain, SceneKit limits the rotation (in any direction) between the initial and target orientations to the `angle` value specified with this method.

The default rotation limit for each joint is 180 degrees in either direction, allowing unconstrained rotation.

## Parameters

- `angle`: The maximum rotation, in degrees, that SceneKit should apply to the specified node when evaluating the constraint.
- `node`: A node affected by the constraint—either the node whose [`constraints`](../scnnode/constraints.md) property references the constraint, or one of that node’s parent or ancestor nodes up to the node specified by the constraint’s [`chainRootNode`](./chainrootnode.md) property.

## See Also

### Adjusting the Constraint’s Limits of Motion
- [var chainRootNode: SCNNode](./chainrootnode.md)
  The parent node of the hierarchy affected by the constraint.
- [func maxAllowedRotationAngle(forJoint: SCNNode) -> CGFloat](./maxallowedrotationangle%28forjoint%29.md)
  Returns the rotation limit, in degrees, for the specified node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnikconstraint/setmaxallowedrotationangle(_:forjoint:))*
# inverseKinematicsConstraint(chainRootNode:)

**Framework**: SceneKit  
**Kind**: method

Creates an inverse kinematics constraint whose chain of nodes begins with the specified node.

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
class func inverseKinematicsConstraint(chainRootNode: SCNNode) -> Self
```

#### Return Value

A new constraint object.

#### Discussion

The root node is the highest node in the hierarchy moved by the constraint. For example, a robot arm may have two arm segments and a hand connected to a body. The upper arm is a child node of the body, the lower arm is a child node of the upper arm, and the hand is a child node of the lower arm. In this case, the upper arm is the chain root node, because the body should not move to follow the hand.

The node you apply the constraint to (using that node’s [`constraints`](scnnode/constraints.md) property) is the  of the chain—the lowest node in the hierarchy. When you set the constraint’s [`targetPosition`](scnikconstraint/targetposition.md) property, SceneKit attempts to move this node toward the target point by rotating it relative to its parent node (and rotating its parent and ancestor nodes, up the chain ending with the `chainRoot` node). Continuing the above example, the end effector of the robot arm is its hand.

## Parameters

- `chainRootNode`: The parent node of the hierarchy to be affected by the constraint.

## See Also

- [init(chainRootNode: SCNNode)](scnikconstraint/init(chainrootnode:).md)
  Initializes an inverse kinematics constraint whose chain of nodes begins with the specified node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnikconstraint/inversekinematicsconstraint(chainrootnode:))*
# SCNIKConstraint

**Framework**: Scenekit  
**Kind**: class

A constraint that applies inverse kinematics to make a chain of nodes “reach” toward a target point.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNIKConstraint
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/f14b291f2a571339e348a8f37f83105e/media-2929777%402x.png)

 is an iterative process that finds positions for the joints connecting a chain of rigid bodies in order to move the body at the end of that chain as close as possible to a desired point in space. For example, a chain of bodies might model a robot arm, and the node at the end of the chain—called an —might model the hand or tool at the end of the arm. To create IK-based behavior in a SceneKit app or game, follow these steps:

1. Build a hierarchy of nodes whose [`position`](scnnode/position.md) and [`pivot`](scnnode/pivot.md) properties describe the joints between them. For example, the node representing a robot’s lower arm should be a child of its upper arm node, and the lower arm node’s [`pivot`](scnnode/pivot.md) property should be placed so that adjusting its [`rotation`](scnnode/rotation.md) property appears to bend the arm at an elbow joint. The robot’s hand should in turn be a child node of the lower arm node.
2. Create an [`SCNIKConstraint`](scnikconstraint.md) object whose [`chainRootNode`](scnikconstraint/chainrootnode.md) property refers to the highest node in the hierarchy whose orientation should be adjusted by the constraint. Continuing the previous example, the root of the chain should be the node containing the upper arm (not the robot’s body, whose orientation remains fixed).
3. Apply the IK constraint to the end effector node of the chain with that node’s [`constraints`](scnnode/constraints.md) property. In the robot arm example, the end effector is the hand or tool at the end of the arm.
4. (Optional) Limit the range of motion of one or more joints in the chain with the [`setMaxAllowedRotationAngle(_:forJoint:)`](scnikconstraint/setmaxallowedrotationangle(_:forjoint:).md) method.
5. To set the constrained nodes in motion, provide a target position for the constraint with its [`targetPosition`](scnikconstraint/targetposition.md) property. You can animate a change to this property

> **Note**:  SceneKit’s physics and inverse kinematics simulations are separate. When SceneKit prepares to render a scene, it processes the physics simulation before applying constraints (including IK constraints). As a result, the effects of an IK constraint override the results of the physics simulation. To use physics with a node also affected by constraints, the node’s [`physicsBody`](scnnode/physicsbody.md) object must be a kinematic physics body.

## Topics

### Creating an Inverse Kinematics Constraint
- [init(chainRootNode: SCNNode)](scnikconstraint/init(chainrootnode:).md)
  Initializes an inverse kinematics constraint whose chain of nodes begins with the specified node.
- [class func inverseKinematicsConstraint(chainRootNode: SCNNode) -> Self](scnikconstraint/inversekinematicsconstraint(chainrootnode:).md)
  Creates an inverse kinematics constraint whose chain of nodes begins with the specified node.
### Adjusting the Constraint’s Limits of Motion
- [var chainRootNode: SCNNode](scnikconstraint/chainrootnode.md)
  The parent node of the hierarchy affected by the constraint.
- [func maxAllowedRotationAngle(forJoint: SCNNode) -> CGFloat](scnikconstraint/maxallowedrotationangle(forjoint:).md)
  Returns the rotation limit, in degrees, for the specified node.
- [func setMaxAllowedRotationAngle(CGFloat, forJoint: SCNNode)](scnikconstraint/setmaxallowedrotationangle(_:forjoint:).md)
  Sets the rotation limit, in degrees, for the specified node.
### Applying Inverse Kinematics to the Constrained Node
- [var targetPosition: SCNVector3](scnikconstraint/targetposition.md)
  The desired position for the constrained node, in the scene’s world coordinate space. Animatable.

## Relationships

### Inherits From
- [SCNConstraint](scnconstraint.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SceneKit/scnikconstraint)*
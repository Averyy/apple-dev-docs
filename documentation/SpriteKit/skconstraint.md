# SKConstraint

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A specification for constraining a node’s position or rotation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SKConstraint
```

```objc
@interface SKConstraint : NSObject
```

## Mentions

- [Working with Inverse Kinematics](./working-with-inverse-kinematics.md)

## Overview

An [`SKConstraint`](./skconstraint.md) object describes a mathematical constraint on a node’s position or orientation. You attach constraints to nodes; after a scene processes any actions and physics interactions, it applies constraints attached to nodes in its node tree. Use constraints to ensure that certain relationships are true before the system renders a scene. For example, you might use a constraint to:

- Change a node’s [`zRotation`](./sknode/zrotation.md) property so that it always points at another node or a position in the scene.
- Keep a node within a specified distance of another node or a point in the scene.
- Keep a node inside a specified rectangle.
- Restrict the [`zRotation`](./sknode/zrotation.md) property of a node so that it has a more limited rotation range of motion.

To use constraints, create an [`NSArray`](../Foundation/nsarray.md) object that contains one or more constraint objects and assign the array to a node’s [`constraints`](./sknode/constraints.md) property. When the system evaluates a scene, it executes the constraints on a node in the order they appear in the [`constraints`](./sknode/constraints.md) array.

You can’t change a constraint after you create it. However, you can selectively disable or enable a constraint by setting its [`enabled`](./skconstraint/enabled.md) property. You can also use the [`referenceNode`](./skconstraint/referencenode.md) property to convert positions to the referenced coordinate system before applying the constraint.

## Topics

### Creating Position Constraints
- [Creating Position Constraints](./creating-position-constraints.md)
  Create a position constraint and add it to a node.
- [class func positionX(SKRange, y: SKRange) -> Self](./skconstraint/positionx%28_,y%29.md)
  Creates a constraint that restricts both coordinates of a node’s position.
- [class func positionX(SKRange) -> Self](./skconstraint/positionx%28_%29.md)
  Creates a constraint that restricts the x-coordinate of a node’s position.
- [class func positionY(SKRange) -> Self](./skconstraint/positiony%28_%29.md)
  Creates a constraint that restricts the y-coordinate of a node’s position.
### Creating Orientation Constraints
- [Creating a Look-At Constraint](./creating-a-look-at-constraint.md)
  Make a node automatically rotate itself based on the changing position of another node, by using orientation constraints.
- [class func orient(to: SKNode, offset: SKRange) -> Self](./skconstraint/orient%28to,offset%29-1h1tw.md)
  Creates a constraint that forces a node to rotate to face another node.
- [class func orient(to: CGPoint, offset: SKRange) -> Self](./skconstraint/orient%28to,offset%29-9lq3h.md)
  Creates a constraint that forces a node to rotate to face a fixed point.
- [class func orient(to: CGPoint, in: SKNode, offset: SKRange) -> Self](./skconstraint/orient%28to,in,offset%29.md)
  Creates a constraint that forces a node to rotate to face a point in another node’s coordinate system.
- [class func zRotation(SKRange) -> Self](./skconstraint/zrotation%28_%29.md)
  Creates a constraint that limits the orientation of a node.
### Creating Distance Constraints
- [class func distance(SKRange, to: SKNode) -> Self](./skconstraint/distance%28_,to%29-6507j.md)
  Creates a constraint that keeps a node within a certain distance of another node.
- [class func distance(SKRange, to: CGPoint) -> Self](./skconstraint/distance%28_,to%29-7yk7n.md)
  Creates a constraint that keeps a node within a certain distance of a point.
- [class func distance(SKRange, to: CGPoint, in: SKNode) -> Self](./skconstraint/distance%28_,to,in%29.md)
  Creates a constraint that keeps a node within a certain distance of a point in another node’s coordinate system.
### Controlling the Coordinate System Where a Constraint is Applied
- [var referenceNode: SKNode?](./skconstraint/referencenode.md)
  The node whose coordinate system should be used to apply the constraint.
### Enabling and Disabling a Constraint
- [var enabled: Bool](./skconstraint/enabled.md)
  A Boolean value that specifies whether the constraint is applied.
### Initializers
- [init?(coder: NSCoder)](./skconstraint/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Constraints
- [class SKReachConstraints](./skreachconstraints.md)
  A specification of the degree of freedom when solving inverse kinematics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint)*
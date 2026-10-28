# SCNLookAtConstraint

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A constraint that orients a node to always point toward a specified other node.

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
class SCNLookAtConstraint
```

```objc
@interface SCNLookAtConstraint : SCNConstraint
```

## Overview

For example, you can use a look-at constraint to ensure that a camera or spotlight always follows the movement of a game character. To attach constraints to an [`SCNNode`](./scnnode.md) object, use its [`constraints`](./scnnode/constraints.md) property.

A node points in the direction of the negative z-axis of its local coordinate system. This axis defines the view direction for nodes containing cameras and the lighting direction for nodes containing spotlights or directional lights, as well as the orientation of the node’s geometry and child nodes. When Scene Kit evaluates a look-at constraint, it updates the constrained node’s [`transform`](./scnnode/transform.md) property so that the node’s negative z-axis points toward the constraint’s target node.

## Topics

### Creating a Look-At Constraint
- [convenience init(target: SCNNode?)](./scnlookatconstraint/init%28target%29.md)
  Creates a look-at constraint for a specified target node.
### Modifying a Constraint
- [var isGimbalLockEnabled: Bool](./scnlookatconstraint/isgimballockenabled.md)
  A Boolean value that specifies whether constrained nodes are allowed to rotate.
- [var target: SCNNode?](./scnlookatconstraint/target.md)
  The node toward which constrained nodes will point after being reoriented.
### Instance Properties
- [var localFront: SCNVector3](./scnlookatconstraint/localfront.md)
- [var targetOffset: SCNVector3](./scnlookatconstraint/targetoffset.md)
- [var worldUp: SCNVector3](./scnlookatconstraint/worldup.md)

## Relationships

### Inherits From
- [SCNConstraint](./scnconstraint.md)
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
- [SCNAnimatable](./scnanimatable.md)

## See Also

### Orientation Constraints
- [class SCNBillboardConstraint](./scnbillboardconstraint.md)
  A constraint that orients a node to always point toward the current camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlookatconstraint)*
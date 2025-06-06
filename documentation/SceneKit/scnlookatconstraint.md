# SCNLookAtConstraint

**Framework**: SceneKit  
**Kind**: class

A constraint that orients a node to always point toward a specified other node.

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
class SCNLookAtConstraint
```

#### Overview

For example, you can use a look-at constraint to ensure that a camera or spotlight always follows the movement of a game character. To attach constraints to an [`SCNNode`](scnnode.md) object, use its [`constraints`](scnnode/constraints.md) property.

A node points in the direction of the negative z-axis of its local coordinate system. This axis defines the view direction for nodes containing cameras and the lighting direction for nodes containing spotlights or directional lights, as well as the orientation of the node’s geometry and child nodes. When Scene Kit evaluates a look-at constraint, it updates the constrained node’s [`transform`](scnnode/transform.md) property so that the node’s negative z-axis points toward the constraint’s target node.

## Topics

### Creating a Look-At Constraint
- [convenience init(target: SCNNode?)](scnlookatconstraint/init(target:).md)
  Creates a look-at constraint for a specified target node.
### Modifying a Constraint
- [var isGimbalLockEnabled: Bool](scnlookatconstraint/isgimballockenabled.md)
  A Boolean value that specifies whether constrained nodes are allowed to rotate.
- [var target: SCNNode?](scnlookatconstraint/target.md)
  The node toward which constrained nodes will point after being reoriented.
### Instance Properties
- [var localFront: SCNVector3](scnlookatconstraint/localfront.md)
- [var targetOffset: SCNVector3](scnlookatconstraint/targetoffset.md)
- [var worldUp: SCNVector3](scnlookatconstraint/worldup.md)

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

## See Also

- [class SCNBillboardConstraint](scnbillboardconstraint.md)
  A constraint that orients a node to always point toward the current camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlookatconstraint)*
# SCNBillboardConstraint

**Framework**: SceneKit  
**Kind**: class

A constraint that orients a node to always point toward the current camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SCNBillboardConstraint
```

#### Overview

An [`SCNBillboardConstraint`](scnbillboardconstraint.md) object automatically adjusts a node’s orientation so that its local z-axis always points toward the [`pointOfView`](scnscenerenderer/pointofview.md) node currently being used to render the scene. For example, you can use a billboard constraint to efficiently render parts of a scene using two-dimensional sprite images instead of three-dimensional geometry—by mapping sprites onto planes affected by a billboard constraint, the sprites maintain their orientation with respect to the viewer. To attach constraints to an [`SCNNode`](scnnode.md) object, use its [`constraints`](scnnode/constraints.md) property.

## Topics

### Working with a Constraint’s Degrees of Freedom
- [var freeAxes: SCNBillboardAxis](scnbillboardconstraint/freeaxes.md)
  An option that specifies which degrees of freedom the constraint affects.
### Constants
- [struct SCNBillboardAxis](scnbillboardaxis.md)
  Options for locking the orientation of nodes affected by a billboard constraint.

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

- [class SCNLookAtConstraint](scnlookatconstraint.md)
  A constraint that orients a node to always point toward a specified other node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint)*
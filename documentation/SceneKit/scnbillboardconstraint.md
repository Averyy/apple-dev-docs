# SCNBillboardConstraint

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A constraint that orients a node to always point toward the current camera.

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
class SCNBillboardConstraint
```

```objc
@interface SCNBillboardConstraint : SCNConstraint
```

## Overview

An [`SCNBillboardConstraint`](./scnbillboardconstraint.md) object automatically adjusts a node’s orientation so that its local z-axis always points toward the [`pointOfView`](./scnscenerenderer/pointofview.md) node currently being used to render the scene. For example, you can use a billboard constraint to efficiently render parts of a scene using two-dimensional sprite images instead of three-dimensional geometry—by mapping sprites onto planes affected by a billboard constraint, the sprites maintain their orientation with respect to the viewer. To attach constraints to an [`SCNNode`](./scnnode.md) object, use its [`constraints`](./scnnode/constraints.md) property.

## Topics

### Working with a Constraint’s Degrees of Freedom
- [var freeAxes: SCNBillboardAxis](./scnbillboardconstraint/freeaxes.md)
  An option that specifies which degrees of freedom the constraint affects.
### Constants
- [struct SCNBillboardAxis](./scnbillboardaxis.md)
  Options for locking the orientation of nodes affected by a billboard constraint.
### Creating a Billboard Constraint
- [+ billboardConstraint](./scnbillboardconstraint/billboardconstraint.md)
  Creates a new billboard constraint.

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
- [class SCNLookAtConstraint](./scnlookatconstraint.md)
  A constraint that orients a node to always point toward a specified other node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint)*
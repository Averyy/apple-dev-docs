# SCNConstraint

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

The abstract superclass for objects that automatically adjust the position, rotation, or scale of a node based on specified rules.

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
class SCNConstraint
```

```objc
@interface SCNConstraint : NSObject
```

#### Overview

To control the transform (position, rotation, and scale) of one or more [`SCNNode`](./scnnode.md) objects with constraints, create and configure instances of the [`SCNConstraint`](./scnconstraint.md) subclass that provides the behavior you want, then add those constraint objects to each node’s [`constraints`](./scnnode/constraints.md) array.

When SceneKit prepares to render a scene, it examines the list of constraints attached to each node to determine the transform for that node, then applies the new transformation before displaying the scene.

## Topics

### Tuning a Constraint’s Effect on Nodes
- [var influenceFactor: CGFloat](./scnconstraint/influencefactor.md)
  The influence of the constraint on the node’s transformation.
### Initializers
- [init?(coder: NSCoder)](./scnconstraint/init%28coder%29.md)
### Instance Properties
- [var isEnabled: Bool](./scnconstraint/isenabled.md)
- [var isIncremental: Bool](./scnconstraint/isincremental.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SCNAccelerationConstraint](./scnaccelerationconstraint.md)
- [SCNAvoidOccluderConstraint](./scnavoidoccluderconstraint.md)
- [SCNBillboardConstraint](./scnbillboardconstraint.md)
- [SCNDistanceConstraint](./scndistanceconstraint.md)
- [SCNIKConstraint](./scnikconstraint.md)
- [SCNLookAtConstraint](./scnlookatconstraint.md)
- [SCNReplicatorConstraint](./scnreplicatorconstraint.md)
- [SCNSliderConstraint](./scnsliderconstraint.md)
- [SCNTransformConstraint](./scntransformconstraint.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnconstraint)*
# SCNConstraint

**Framework**: SceneKit  
**Kind**: class

The abstract superclass for objects that automatically adjust the position, rotation, or scale of a node based on specified rules.

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
class SCNConstraint
```

#### Overview

To control the transform (position, rotation, and scale) of one or more [`SCNNode`](scnnode.md) objects with constraints, create and configure instances of the [`SCNConstraint`](scnconstraint.md) subclass that provides the behavior you want, then add those constraint objects to each node’s [`constraints`](scnnode/constraints.md) array.

When SceneKit prepares to render a scene, it examines the list of constraints attached to each node to determine the transform for that node, then applies the new transformation before displaying the scene.

## Topics

### Tuning a Constraint’s Effect on Nodes
- [var influenceFactor: CGFloat](scnconstraint/influencefactor.md)
  The influence of the constraint on the node’s transformation.
### Instance Properties
- [var isEnabled: Bool](scnconstraint/isenabled.md)
- [var isIncremental: Bool](scnconstraint/isincremental.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SCNAccelerationConstraint](scnaccelerationconstraint.md)
- [SCNAvoidOccluderConstraint](scnavoidoccluderconstraint.md)
- [SCNBillboardConstraint](scnbillboardconstraint.md)
- [SCNDistanceConstraint](scndistanceconstraint.md)
- [SCNIKConstraint](scnikconstraint.md)
- [SCNLookAtConstraint](scnlookatconstraint.md)
- [SCNReplicatorConstraint](scnreplicatorconstraint.md)
- [SCNSliderConstraint](scnsliderconstraint.md)
- [SCNTransformConstraint](scntransformconstraint.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnconstraint)*
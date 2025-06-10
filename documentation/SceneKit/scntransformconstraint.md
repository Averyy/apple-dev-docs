# SCNTransformConstraint

**Framework**: SceneKit  
**Kind**: class

A constraint that runs a specified closure, block in Objective-C, to compute a new transform (position, rotation, and scale) for each node that the constraint affects.

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
class SCNTransformConstraint
```

#### Overview

To attach constraints to an [`SCNNode`](scnnode.md) object, use its [`constraints`](scnnode/constraints.md) property.

When Scene Kit prepares to render a scene, it evaluates the list of constraints attached to each node to determine the transformation for that node, then applies the new transformation before rendering. To evaluate a transform constraint, Scene Kit runs the block you provided when creating the constraint. In this block, your app computes a new transformation to be applied to the node. Optionally, your app may reference the node’s current transformation in computing the new transformation.

## Topics

### Creating a Transform Constraint
- [convenience init(inWorldSpace: Bool, with: (SCNNode, SCNMatrix4) -> SCNMatrix4)](scntransformconstraint/init(inworldspace:with:).md)
  Creates a new transform constraint.
### Type Methods
- [class func orientationConstraint(inWorldSpace: Bool, with: (SCNNode, SCNQuaternion) -> SCNQuaternion) -> Self](scntransformconstraint/orientationconstraint(inworldspace:with:).md)
- [class func positionConstraint(inWorldSpace: Bool, with: (SCNNode, SCNVector3) -> SCNVector3) -> Self](scntransformconstraint/positionconstraint(inworldspace:with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransformconstraint)*
# SCNTransformConstraint

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A constraint that runs a specified closure, block in Objective-C, to compute a new transform (position, rotation, and scale) for each node that the constraint affects.

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
class SCNTransformConstraint
```

```objc
@interface SCNTransformConstraint : SCNConstraint
```

#### Overview

To attach constraints to an [`SCNNode`](./scnnode.md) object, use its [`constraints`](./scnnode/constraints.md) property.

When Scene Kit prepares to render a scene, it evaluates the list of constraints attached to each node to determine the transformation for that node, then applies the new transformation before rendering. To evaluate a transform constraint, Scene Kit runs the block you provided when creating the constraint. In this block, your app computes a new transformation to be applied to the node. Optionally, your app may reference the node’s current transformation in computing the new transformation.

## Topics

### Creating a Transform Constraint
- [convenience init(inWorldSpace: Bool, with: (SCNNode, SCNMatrix4) -> SCNMatrix4)](./scntransformconstraint/init%28inworldspace,with%29.md)
  Creates a new transform constraint.
### Initializers
- [convenience init(inWorldSpace: Bool, withBlock: (SCNNode, SCNMatrix4) -> SCNMatrix4)](./scntransformconstraint/init%28inworldspace,withblock%29.md)
### Type Methods
- [class func orientationConstraint(inWorldSpace: Bool, with: (SCNNode, SCNQuaternion) -> SCNQuaternion) -> Self](./scntransformconstraint/orientationconstraint%28inworldspace,with%29.md)
- [class func positionConstraint(inWorldSpace: Bool, with: (SCNNode, SCNVector3) -> SCNVector3) -> Self](./scntransformconstraint/positionconstraint%28inworldspace,with%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransformconstraint)*
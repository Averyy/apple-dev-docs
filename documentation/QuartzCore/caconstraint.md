# CAConstraint

**Framework**: Core Animation  
**Kind**: class

A representation of a single layout constraint between two layers.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
class CAConstraint
```

#### Overview

Each [`CAConstraint`](caconstraint.md) instance encapsulates one geometry relationship between two layers on the same axis.

Sibling layers are referenced by name, using the name property of each layer. The special name `superlayer` is used to refer to the layer’s superlayer.

For example, to specify that a layer should be horizontally centered in its superview you would use the following:

A minimum of two relationships must be specified per axis. If you specify constraints for the left and right edges of a layer, the width will vary. If you specify constraints for the left edge and the width, the right edge of the layer will move relative to the superlayer’s frame. Often you’ll specify only a single edge constraint, the layer’s size in the same axis will be used as the second relationship.

> ❗ **Important**:  It is possible to create constraints that result in circular references to the same attributes. In cases where the layout is unable to be computed the behavior is undefined.

## Topics

### Create a New Constraint
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, offset: CGFloat)](caconstraint/init(attribute:relativeto:attribute:offset:).md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute)](caconstraint/init(attribute:relativeto:attribute:).md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, scale: CGFloat, offset: CGFloat)](caconstraint/init(attribute:relativeto:attribute:scale:offset:).md)
  Returns an `CAConstraint` object with the specified parameters. Designated initializer.
### Accessing Constraint Values
- [var attribute: CAConstraintAttribute](caconstraint/attribute.md)
  The attribute the constraint affects.
- [var offset: CGFloat](caconstraint/offset.md)
  Offset value of the constraint attribute.
- [var scale: CGFloat](caconstraint/scale.md)
  Scale factor of the constraint attribute.
- [var sourceAttribute: CAConstraintAttribute](caconstraint/sourceattribute.md)
  The constraint attribute of the layer the receiver is calculated relative to
- [var sourceName: String](caconstraint/sourcename.md)
  Name of the layer that the constraint is calculated relative to.
### Constants
- [enum CAConstraintAttribute](caconstraintattribute.md)
  The constraint attribute type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CALayer](calayer.md)
  An object that manages image-based content and allows you to perform animations on that content.
- [protocol CALayerDelegate](calayerdelegate.md)
  Methods your app can implement to respond to layer-related events.
- [protocol CALayoutManager](calayoutmanager.md)
  Methods that allow an object to manage the layout of a layer and its sublayers.
- [class CAConstraintLayoutManager](caconstraintlayoutmanager.md)
  An object that provides a constraint-based layout manager.
- [protocol CAAction](caaction.md)
  An interface that allows instances to respond to actions triggered by a Core Animation layer change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraint)*
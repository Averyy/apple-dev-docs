# NSLayoutConstraint.Relation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The relation between the first attribute and the modified second attribute in a constraint.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Relation
```

```c
enum NSLayoutRelation : NSInteger;
```

## Topics

### Constants
- [NSLayoutConstraint.Relation.lessThanOrEqual](./relation-swift.enum/lessthanorequal.md)
  The constraint requires the first attribute to be less than or equal to the modified second attribute.
- [NSLayoutConstraint.Relation.equal](./relation-swift.enum/equal.md)
  The constraint requires the first attribute to be exactly equal to the modified second attribute.
- [NSLayoutConstraint.Relation.greaterThanOrEqual](./relation-swift.enum/greaterthanorequal.md)
  The constraint requires the first attribute to be greater than or equal to the modified second attribute.
### Initializers
- [init?(rawValue: Int)](./relation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSLayoutConstraint.Attribute](./attribute.md)
  The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.FormatOptions](./formatoptions.md)
  A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../../AppKit/nslayoutconstraint/orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [NSLayoutConstraint.Axis](./axis.md)
  Keys that specify a horizontal or vertical layout constraint between objects.
- [struct NSEdgeInsets](../../Foundation/nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.
- [var NSLAYOUTCONSTRAINT_H: Int32](../nslayoutconstraint_h.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation-swift.enum)*
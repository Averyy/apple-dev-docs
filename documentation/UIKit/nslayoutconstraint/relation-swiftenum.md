# NSLayoutConstraint.Relation

**Framework**: UIKit  
**Kind**: enum

The relation between the first attribute and the modified second attribute in a constraint.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Relation
```

## Topics

### Constants
- [NSLayoutConstraint.Relation.lessThanOrEqual](nslayoutconstraint/relation-swift.enum/lessthanorequal.md)
  The constraint requires the first attribute to be less than or equal to the modified second attribute.
- [NSLayoutConstraint.Relation.equal](nslayoutconstraint/relation-swift.enum/equal.md)
  The constraint requires the first attribute to be exactly equal to the modified second attribute.
- [NSLayoutConstraint.Relation.greaterThanOrEqual](nslayoutconstraint/relation-swift.enum/greaterthanorequal.md)
  The constraint requires the first attribute to be greater than or equal to the modified second attribute.
### Initializers
- [init?(rawValue: Int)](nslayoutconstraint/relation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSLayoutConstraint.Attribute](nslayoutconstraint/attribute.md)
  The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions.md)
  A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../AppKit/NSLayoutConstraint/Orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [NSLayoutConstraint.Axis](nslayoutconstraint/axis.md)
  Keys that specify a horizontal or vertical layout constraint between objects.
- [struct NSEdgeInsets](../Foundation/NSEdgeInsets.md)
  A description of the distance between the edges of two rectangles.
- [var NSLAYOUTCONSTRAINT_H: Int32](nslayoutconstraint_h.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation-swift.enum)*
# NSLayoutConstraint.Attribute

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The part of the object’s visual representation that should be used to get the value for the constraint.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Attribute
```

```c
enum NSLayoutAttribute : NSInteger;
```

## Topics

### Constants
- [NSLayoutConstraint.Attribute.left](./attribute/left.md)
  The left side of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.right](./attribute/right.md)
  The right side of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.top](./attribute/top.md)
  The top of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.bottom](./attribute/bottom.md)
  The bottom of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.leading](./attribute/leading.md)
  The leading edge of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.trailing](./attribute/trailing.md)
  The trailing edge of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.width](./attribute/width.md)
  The width of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.height](./attribute/height.md)
  The height of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.centerX](./attribute/centerx.md)
  The center along the x-axis of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.centerY](./attribute/centery.md)
  The center along the y-axis of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.lastBaseline](./attribute/lastbaseline.md)
  The object’s baseline.
- [NSLayoutConstraint.Attribute.firstBaseline](./attribute/firstbaseline.md)
  The object’s baseline.
- [NSLayoutConstraint.Attribute.leftMargin](./attribute/leftmargin.md)
  The object’s left margin.
- [NSLayoutConstraint.Attribute.rightMargin](./attribute/rightmargin.md)
  The object’s right margin.
- [NSLayoutConstraint.Attribute.topMargin](./attribute/topmargin.md)
  The object’s top margin.
- [NSLayoutConstraint.Attribute.bottomMargin](./attribute/bottommargin.md)
  The object’s bottom margin.
- [NSLayoutConstraint.Attribute.leadingMargin](./attribute/leadingmargin.md)
  The object’s leading margin.
- [NSLayoutConstraint.Attribute.trailingMargin](./attribute/trailingmargin.md)
  The object’s trailing margin.
- [NSLayoutConstraint.Attribute.centerXWithinMargins](./attribute/centerxwithinmargins.md)
  The center along the x-axis between the object’s left and right margin.
- [NSLayoutConstraint.Attribute.centerYWithinMargins](./attribute/centerywithinmargins.md)
  The center along the y-axis between the object’s top and bottom margin.
- [NSLayoutConstraint.Attribute.notAnAttribute](./attribute/notanattribute.md)
  A placeholder value for indicating that the constraint’s second item and second attribute aren’t used in any calculations.
- [NSLayoutAttributeBaseline](../nslayoutattribute/nslayoutattributebaseline.md)
  The object’s baseline.
### Initializers
- [init?(rawValue: Int)](./attribute/init%28rawvalue%29.md)

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
- [NSLayoutConstraint.Relation](./relation-swift.enum.md)
  The relation between the first attribute and the modified second attribute in a constraint.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute)*
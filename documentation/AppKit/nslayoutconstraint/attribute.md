# NSLayoutConstraint.Attribute

**Framework**: AppKit  
**Kind**: enum

The part of the object’s visual representation that should be used to get the value for the constraint.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Attribute
```

## Topics

### Constants
- [NSLayoutConstraint.Attribute.left](nslayoutconstraint/attribute/left.md)
  The left side of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.right](nslayoutconstraint/attribute/right.md)
  The right side of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.top](nslayoutconstraint/attribute/top.md)
  The top of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.bottom](nslayoutconstraint/attribute/bottom.md)
  The bottom of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.leading](nslayoutconstraint/attribute/leading.md)
  The leading edge of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.trailing](nslayoutconstraint/attribute/trailing.md)
  The trailing edge of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.width](nslayoutconstraint/attribute/width.md)
  The width of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.height](nslayoutconstraint/attribute/height.md)
  The height of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.centerX](nslayoutconstraint/attribute/centerx.md)
  The center along the x-axis of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.centerY](nslayoutconstraint/attribute/centery.md)
  The center along the y-axis of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.lastBaseline](nslayoutconstraint/attribute/lastbaseline.md)
  The object’s baseline.
- [NSLayoutConstraint.Attribute.firstBaseline](nslayoutconstraint/attribute/firstbaseline.md)
  The object’s baseline.
- [NSLayoutConstraint.Attribute.notAnAttribute](nslayoutconstraint/attribute/notanattribute.md)
  A placeholder value for indicating that the constraint’s second item and second attribute aren’t used in any calculations.
### Initializers
- [init?(rawValue: Int)](nslayoutconstraint/attribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSLayoutConstraint.Relation](nslayoutconstraint/relation-swift.enum.md)
  The relation between the first attribute and the modified second attribute in a constraint.
- [NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions.md)
  A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](nslayoutconstraint/orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [struct NSEdgeInsets](../Foundation/NSEdgeInsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute)*
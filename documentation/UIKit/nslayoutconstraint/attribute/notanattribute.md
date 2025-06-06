# NSLayoutConstraint.Attribute.notAnAttribute

**Framework**: UIKit  
**Kind**: case

A placeholder value for indicating that the constraint’s second item and second attribute aren’t used in any calculations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case notAnAttribute
```

#### Discussion

Use this value when creating a constraint that assigns a constant to an attribute. For example, `item1.height >= 40`. If a constraint only has one item, set the second item to `nil`, and set the second attribute to [`NSLayoutConstraint.Attribute.notAnAttribute`](nslayoutconstraint/attribute/notanattribute.md).

## See Also

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
- [NSLayoutConstraint.Attribute.leftMargin](nslayoutconstraint/attribute/leftmargin.md)
  The object’s left margin.
- [NSLayoutConstraint.Attribute.rightMargin](nslayoutconstraint/attribute/rightmargin.md)
  The object’s right margin.
- [NSLayoutConstraint.Attribute.topMargin](nslayoutconstraint/attribute/topmargin.md)
  The object’s top margin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/notanattribute)*
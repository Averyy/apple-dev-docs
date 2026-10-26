# NSLayoutConstraint.Attribute.notAnAttribute

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A placeholder value for indicating that the constraint’s second item and second attribute aren’t used in any calculations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case notAnAttribute
```

```c
NSLayoutAttributeNotAnAttribute
```

#### Discussion

Use this value when creating a constraint that assigns a constant to an attribute. For example, `item1.height >= 40`. If a constraint only has one item, set the second item to `nil`, and set the second attribute to [`NSLayoutConstraint.Attribute.notAnAttribute`](./notanattribute.md).

## See Also

### Constants
- [NSLayoutConstraint.Attribute.left](./left.md)
  The left side of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.right](./right.md)
  The right side of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.top](./top.md)
  The top of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.bottom](./bottom.md)
  The bottom of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.leading](./leading.md)
  The leading edge of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.trailing](./trailing.md)
  The trailing edge of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.width](./width.md)
  The width of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.height](./height.md)
  The height of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.centerX](./centerx.md)
  The center along the x-axis of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.centerY](./centery.md)
  The center along the y-axis of the object’s alignment rectangle.
- [NSLayoutConstraint.Attribute.lastBaseline](./lastbaseline.md)
  The object’s baseline.
- [NSLayoutConstraint.Attribute.firstBaseline](./firstbaseline.md)
  The object’s baseline.
- [NSLayoutConstraint.Attribute.leftMargin](./leftmargin.md)
  The object’s left margin.
- [NSLayoutConstraint.Attribute.rightMargin](./rightmargin.md)
  The object’s right margin.
- [NSLayoutConstraint.Attribute.topMargin](./topmargin.md)
  The object’s top margin.
- [NSLayoutAttributeBaseline](../../nslayoutattribute/nslayoutattributebaseline.md)
  The object’s baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/notanattribute)*
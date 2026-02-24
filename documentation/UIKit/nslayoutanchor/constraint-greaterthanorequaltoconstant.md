# constraint(greaterThanOrEqualTo:constant:)

**Framework**: UIKit  
**Kind**: method

Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func constraint(greaterThanOrEqualTo anchor: NSLayoutAnchor<AnchorType>, constant c: CGFloat) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that defines the attribute represented by this layout anchor as greater than or equal to the attribute represented by the `anchor` parameter plus a constant offset.

#### Discussion

This method defines the relationship `first attribute >= second attribute + c`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter. The value `c`, represents a constant offset. All values are measured in points; however, these values can be interpreted in different ways, depending on the type of layout anchor.

- For [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) objects, the first attribute is positioned `c` points after the second attribute. When using leading or trailing attributes, values increase as you move in the language’s reading direction. In English, for example, values increase as you move to the right. For left and right attributes, values always increase as you move right.
- For [`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) objects, the first attribute is positioned `c` points below the second attribute. Values increase as you move down.
- For [`NSLayoutDimension`](nslayoutdimension.md) objects, the size of the first attribute is `c` points larger than the size of the second attribute. Values increase as items increase in size.

The constraints produced by the following two examples are identical.

**Swift**:

```swift
// Creating a constraint using NSLayoutConstraint
 
NSLayoutConstraint(item: textField,
                   attribute: .Leading,
                   relatedBy: .GreaterThanOrEqual,
                   toItem: label,
                   attribute: .Trailing,
                   multiplier: 1.0,
                   constant: 8.0).isActive = true
 
// Creating the same constraint using constraintGreaterThanOrEqualToAnchor:constant:
textField.leadingAnchor.constraintGreaterThanOrEqualToAnchor(label.trailingAnchor, constant: 8.0).isActive = true
```

**Objective-C**:

```objc
// Creating a constraint using NSLayoutConstraint
 
[NSLayoutConstraint constraintWithItem:self.textField
                             attribute:NSLayoutAttributeLeading
                             relatedBy:NSLayoutRelationGreaterThanOrEqual
                                toItem:self.label
                             attribute:NSLayoutAttributeTrailing
                            multiplier:1.0
                              constant:8.0].active = YES;
 
// Creating the same constraint using constraintGreaterThanOrEqualToAnchor:constant:
[self.textField.leadingAnchor constraintGreaterThanOrEqualToAnchor:self.label.trailingAnchor constant:8.0].active = YES;
```

## Parameters

- `anchor`: A layout anchor from a [`UIView`](uiview.md), [`NSView`](https://developer.apple.com/documentation/AppKit/NSView), or [`UILayoutGuide`](uilayoutguide.md) object. You must use a subclass of [`NSLayoutAnchor`](nslayoutanchor.md) that matches the current anchor. For example, if you call this method on an [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) object, this parameter must be another [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md).
- `c`: The constant offset for the constraint.

## See Also

- [func constraint(equalTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:).md)
  Returns a constraint that defines one item’s attribute as equal to another.
- [func constraint(equalTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:constant:).md)
  Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutanchor/constraint(greaterthanorequalto:constant:))*
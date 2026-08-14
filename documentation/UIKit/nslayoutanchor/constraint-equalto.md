# constraint(equalTo:)

**Framework**: UIKit  
**Kind**: method

Returns a constraint that defines one item’s attribute as equal to another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func constraint(equalTo anchor: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that defines an equal relationship between the attributes represented by the two layout anchors.

#### Discussion

This method defines the relationship `first attribute = second attribute`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter.

The constraints produced by the following two examples are identical.

**Swift**:

```swift
// Creating a constraint using NSLayoutConstraint
NSLayoutConstraint(item: subview,
                   attribute: .Leading,
                   relatedBy: .Equal,
                   toItem: view,
                   attribute: .LeadingMargin,
                   multiplier: 1.0,
                   constant: 0.0).isActive = true
 
// Creating the same constraint using constraintEqualToAnchor:
let margins = view.layoutMarginsGuide
subview.leadingAnchor.constraintEqualToAnchor(margins.leadingAnchor).isActive = true
```

**Objective-C**:

```objc
// Creating a constraint using NSLayoutConstraint
[NSLayoutConstraint
 constraintWithItem:subview
 attribute:NSLayoutAttributeLeading
 relatedBy:NSLayoutRelationEqual
 toItem:self.view
 attribute:NSLayoutAttributeLeadingMargin
 multiplier:1.0
 constant:0.0].active = YES;
 
// Creating the same constraint using constraintEqualToAnchor:
UILayoutGuide *margin = self.view.layoutMarginsGuide;
[subview.leadingAnchor constraintEqualToAnchor:margin.leadingAnchor].active = YES;
```

## Parameters

- `anchor`: A layout anchor from a [`UIView`](uiview.md), [`NSView`](https://developer.apple.com/documentation/appkit/nsview), or [`UILayoutGuide`](uilayoutguide.md) object. You must use a subclass of [`NSLayoutAnchor`](nslayoutanchor.md) that matches the current anchor. For example, if you call this method on an [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) object, this parameter must be another [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md).

## See Also

- [func constraint(equalTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:constant:).md)
  Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutanchor/constraint(equalto:))*
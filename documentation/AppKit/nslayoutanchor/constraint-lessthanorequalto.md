# constraint(lessThanOrEqualTo:)

**Framework**: AppKit  
**Kind**: method

Returns a constraint that defines one item’s attribute as less than or equal to another.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func constraint(lessThanOrEqualTo anchor: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that defines the attribute represented by this layout anchor as less than or equal to the attribute represented by the `anchor` parameter.

#### Discussion

This method defines the relationship `first attribute <= second attribute`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter. All values are measured in points; however, these values can be interpreted in different ways, depending on the type of layout anchor.

- For leading or trailing anchors, the values increase as you move in the current language’s reading direction. For English, values increase as you move to the right.
- For left and right anchors, the values increase as you move to the right.
- For [`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) objects, the values increase as you move down.
- For [`NSLayoutDimension`](nslayoutdimension.md) objects, the values increase as the items increase in size.

The constraints produced by the following two examples are identical.

## Parameters

- `anchor`: A layout anchor from an   or   object. You must use a subclass of   that matches the current anchor. For example, if you call this method on an   object, this parameter must be another  .

## See Also

- [func constraint(equalTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:).md)
  Returns a constraint that defines one item’s attribute as equal to another.
- [func constraint(equalTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:constant:).md)
  Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutanchor/constraint(lessthanorequalto:))*
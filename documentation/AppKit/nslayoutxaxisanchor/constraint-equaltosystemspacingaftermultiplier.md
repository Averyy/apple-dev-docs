# constraint(equalToSystemSpacingAfter:multiplier:)

**Framework**: AppKit  
**Kind**: method

Returns a constraint that defines by how much the current anchor trails the specified anchor.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func constraint(equalToSystemSpacingAfter anchor: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that imposes a specific distance between the current anchor and the object in the `anchor` parameter.

#### Discussion

The constraint causes the current anchor to trail the object in the `anchor` parameter. For example, in a left-to-right layout, the current anchor is to the right of `anchor`, but in a right-to-left layout, it’s to the left of `anchor`.

The distance between the two anchors is determined by multiplying the system spacing by the value in the `multiplier` parameter. The value of the system space is determined from information available from the anchors.

## Parameters

- `anchor`: The anchor to use as the starting point for the constraint.
- `multiplier`: The multiple of the system spacing to use as the distance between the two anchors.

## See Also

- [func constraint(greaterThanOrEqualToSystemSpacingAfter: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutxaxisanchor/constraint(greaterthanorequaltosystemspacingafter:multiplier:).md)
  Returns a constraint that defines the minimum amount by which the current anchor trails the specified anchor.
- [func constraint(lessThanOrEqualToSystemSpacingAfter: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutxaxisanchor/constraint(lessthanorequaltosystemspacingafter:multiplier:).md)
  Returns a constraint that defines the maximum amount by which the current anchor trails the specified anchor.
- [Creating self-sizing table view cells](../UIKit/creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutxaxisanchor/constraint(equaltosystemspacingafter:multiplier:))*
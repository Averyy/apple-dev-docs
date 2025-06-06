# constraint(lessThanOrEqualToSystemSpacingBelow:multiplier:)

**Framework**: AppKit  
**Kind**: method

Returns a constraint that defines the maximum distance by which the current anchor is positioned below the specified anchor.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func constraint(lessThanOrEqualToSystemSpacingBelow anchor: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that imposes a minimum distance between the current anchor and the object in the `anchor` parameter.

#### Discussion

The constraint causes the current anchor to be positioned below the object in the `anchor` parameter. The maximum distance between the two anchors is determined by multiplying the system spacing by the value in the `multiplier` parameter. The value of the system spacing is determined from information available from the anchors. For example, if the anchors represent text baselines, the spacing is determined by the fonts used at those baselines.

## Parameters

- `anchor`: The anchor to use as the starting point for the constraint.
- `multiplier`: The multiple of the system spacing to use as the distance between the two anchors.

## See Also

- [func constraint(equalToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(equaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the specific distance at which the current anchor is positioned below the specified anchor.
- [func constraint(greaterThanOrEqualToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(greaterthanorequaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the minimum distance by which the current anchor is positioned below the specified anchor.
- [Creating self-sizing table view cells](../UIKit/creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutyaxisanchor/constraint(lessthanorequaltosystemspacingbelow:multiplier:))*
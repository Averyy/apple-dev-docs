# constraint(equalToSystemSpacingBelow:multiplier:)

**Framework**: UIKit  
**Kind**: method

Returns a constraint that defines the specific distance at which the current anchor is positioned below the specified anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func constraint(equalToSystemSpacingBelow anchor: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that imposes a specific distance between the current anchor and the object in the `anchor` parameter.

#### Discussion

The constraint causes the current anchor to be positioned below the object in the `anchor` parameter. The distance between the two anchors is determined by multiplying the system spacing by the value in the `multiplier` parameter. The value of the system spacing is determined from information available from the anchors. For example, if the anchors represent text baselines, the spacing is determined by the fonts used at those baselines.

## Parameters

- `anchor`: The anchor to use as the starting point for the constraint.
- `multiplier`: The multiple of the system spacing to use as the distance between the two anchors.

## See Also

- [func constraint(greaterThanOrEqualToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(greaterthanorequaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the minimum distance by which the current anchor is positioned below the specified anchor.
- [func constraint(lessThanOrEqualToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(lessthanorequaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the maximum distance by which the current anchor is positioned below the specified anchor.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor/constraint(equaltosystemspacingbelow:multiplier:))*
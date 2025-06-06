# addConstraint(_:)

**Framework**: AppKit  
**Kind**: method

Adds a constraint on the layout of the receiving view or its subviews.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func addConstraint(_ constraint: NSLayoutConstraint)
```

#### Discussion

The constraint must involve only views that are within scope of the receiving view. Specifically, any views involved must be either the receiving view itself, or a subview of the receiving view. Constraints that are added to a view are said to be held by that view. The coordinate system used when evaluating the constraint is the coordinate system of the view that holds the constraint.

## Parameters

- `constraint`: The constraint to be added to the view. The constraint may only reference the view itself or its subviews.

## See Also

- [var constraints: [NSLayoutConstraint]](nsview/constraints.md)
  Returns the constraints held by the view.
- [func addConstraints([NSLayoutConstraint])](nsview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](nsview/removeconstraint(_:).md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](nsview/removeconstraints(_:).md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addconstraint(_:))*
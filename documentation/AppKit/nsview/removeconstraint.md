# removeConstraint(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified constraint from the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func removeConstraint(_ constraint: NSLayoutConstraint)
```

## Parameters

- `constraint`: The constraint to remove. Removing a constraint not held by the view has no effect.

## See Also

- [var constraints: [NSLayoutConstraint]](nsview/constraints.md)
  Returns the constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](nsview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](nsview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraints([NSLayoutConstraint])](nsview/removeconstraints(_:).md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removeconstraint(_:))*
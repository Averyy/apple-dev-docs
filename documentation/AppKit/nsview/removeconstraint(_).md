# removeConstraint(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified constraint from the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func removeConstraint(_ constraint: NSLayoutConstraint)
```

```objc
- (void) removeConstraint:(NSLayoutConstraint *) constraint;
```

## Parameters

- `constraint`: The constraint to remove. Removing a constraint not held by the view has no effect.

## See Also

### Managing the View’s Constraints
- [var constraints: [NSLayoutConstraint]](./constraints.md)
  Returns the constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](./addconstraint%28_%29.md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](./addconstraints%28_%29.md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraints([NSLayoutConstraint])](./removeconstraints%28_%29.md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removeconstraint(_:))*
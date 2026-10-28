# addConstraints(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds multiple constraints on the layout of the receiving view or its subviews.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func addConstraints(_ constraints: [NSLayoutConstraint])
```

```objc
- (void) addConstraints:(NSArray<NSLayoutConstraint *> *) constraints;
```

## Discussion

All constraints must involve only views that are within scope of the receiving view. Specifically, any views involved must be either the receiving view itself, or a subview of the receiving view. Constraints that are added to a view are said to be held by that view. The coordinate system used when evaluating each constraint is the coordinate system of the view that holds the constraint.

## Parameters

- `constraints`: An array of constraints to be added to the view. All constraints may only reference the view itself or its subviews.

## See Also

### Managing the View’s Constraints
- [var constraints: [NSLayoutConstraint]](./constraints.md)
  Returns the constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](./addconstraint%28_%29.md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](./removeconstraint%28_%29.md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](./removeconstraints%28_%29.md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addconstraints(_:))*
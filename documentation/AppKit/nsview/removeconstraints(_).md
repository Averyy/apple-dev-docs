# removeConstraints(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified constraints from the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func removeConstraints(_ constraints: [NSLayoutConstraint])
```

```objc
- (void) removeConstraints:(NSArray<NSLayoutConstraint *> *) constraints;
```

## Parameters

- `constraints`: The constraints to remove.

## See Also

### Managing the View’s Constraints
- [var constraints: [NSLayoutConstraint]](./constraints.md)
  Returns the constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](./addconstraint%28_%29.md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](./addconstraints%28_%29.md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](./removeconstraint%28_%29.md)
  Removes the specified constraint from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removeconstraints(_:))*
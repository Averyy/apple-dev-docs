# constraints

**Framework**: AppKit  
**Kind**: property

Returns the constraints held by the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var constraints: [NSLayoutConstraint] { get }
```

#### Return Value

The constraints held by the view.

## See Also

- [func addConstraint(NSLayoutConstraint)](nsview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](nsview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](nsview/removeconstraint(_:).md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](nsview/removeconstraints(_:).md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/constraints)*
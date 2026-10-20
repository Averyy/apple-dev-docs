# constraints

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the constraints held by the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var constraints: [NSLayoutConstraint] { get }
```

```objc
@property (copy, readonly) NSArray<NSLayoutConstraint *> * constraints;
```

#### Return Value

The constraints held by the view.

## See Also

### Managing the View’s Constraints
- [func addConstraint(NSLayoutConstraint)](./addconstraint%28_%29.md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](./addconstraints%28_%29.md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](./removeconstraint%28_%29.md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](./removeconstraints%28_%29.md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/constraints)*
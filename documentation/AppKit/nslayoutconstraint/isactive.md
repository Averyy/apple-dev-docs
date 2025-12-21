# isActive

**Framework**: AppKit  
**Kind**: property

The active state of the constraint.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isActive: Bool { get set }
```

#### Discussion

You can activate or deactivate a constraint by changing this property. Note that only active constraints affect the calculated layout. If you try to activate a constraint whose items have no common ancestor, an exception is thrown. For newly created constraints, the [`isActive`](nslayoutconstraint/isactive.md) property is [`false`](https://developer.apple.com/documentation/Swift/false) by default.

Activating or deactivating the constraint calls [`addConstraint(_:)`](nsview/addconstraint(_:).md) and [`removeConstraint(_:)`](nsview/removeconstraint(_:).md) on the view that is the closest common ancestor of the items managed by this constraint. Use this property instead of calling [`addConstraint(_:)`](nsview/addconstraint(_:).md) or [`removeConstraint(_:)`](nsview/removeconstraint(_:).md) directly.

## See Also

- [class func activate([NSLayoutConstraint])](nslayoutconstraint/activate(_:).md)
  Activates each constraint in the specified array.
- [class func deactivate([NSLayoutConstraint])](nslayoutconstraint/deactivate(_:).md)
  Deactivates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/isactive)*
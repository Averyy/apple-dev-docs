# isActive

**Framework**: UIKit  
**Kind**: property

The active state of the constraint.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isActive: Bool { get set }
```

#### Discussion

You can activate or deactivate a constraint by changing this property. Note that only active constraints affect the calculated layout. If you try to activate a constraint whose items have no common ancestor, an exception is thrown. For newly created constraints, the [`isActive`](nslayoutconstraint/isactive.md) property is [`false`](https://developer.apple.com/documentation/swift/false) by default.

Activating or deactivating the constraint calls [`addConstraint(_:)`](uiview/addconstraint(_:).md) and [`removeConstraint(_:)`](uiview/removeconstraint(_:).md) on the view that is the closest common ancestor of the items managed by this constraint. Use this property instead of calling [`addConstraint(_:)`](uiview/addconstraint(_:).md) or [`removeConstraint(_:)`](uiview/removeconstraint(_:).md) directly.

## See Also

- [class func activate([NSLayoutConstraint])](nslayoutconstraint/activate(_:).md)
  Activates each constraint in the specified array.
- [class func deactivate([NSLayoutConstraint])](nslayoutconstraint/deactivate(_:).md)
  Deactivates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/isactive)*
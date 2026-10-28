# isActive

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The active state of the constraint.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get set }
```

```objc
@property (getter=isActive) BOOL active;
```

## Discussion

You can activate or deactivate a constraint by changing this property. Note that only active constraints affect the calculated layout. If you try to activate a constraint whose items have no common ancestor, an exception is thrown. For newly created constraints, the [`isActive`](./isactive.md) property is [`false`](../../Swift/false.md) by default.

Activating or deactivating the constraint calls [`addConstraint(_:)`](../uiview/addconstraint%28_%29.md) and [`removeConstraint(_:)`](../uiview/removeconstraint%28_%29.md) on the view that is the closest common ancestor of the items managed by this constraint. Use this property instead of calling [`addConstraint(_:)`](../uiview/addconstraint%28_%29.md) or [`removeConstraint(_:)`](../uiview/removeconstraint%28_%29.md) directly.

## See Also

### Activating and deactivating constraints
- [class func activate([NSLayoutConstraint])](./activate%28_%29.md)
  Activates each constraint in the specified array.
- [class func deactivate([NSLayoutConstraint])](./deactivate%28_%29.md)
  Deactivates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/isactive)*
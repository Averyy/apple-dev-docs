# activate(_:)

**Framework**: AppKit  
**Kind**: method

Activates each constraint in the specified array.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func activate(_ constraints: [NSLayoutConstraint])
```

#### Discussion

This convenience method provides an easy way to activate a set of constraints with one call. The effect of this method is the same as setting the [`isActive`](nslayoutconstraint/isactive.md) property of each constraint to [`true`](https://developer.apple.com/documentation/swift/true). Typically, using this method is more efficient than activating each constraint individually.

## Parameters

- `constraints`: An array of constraints to activate.

## See Also

- [var isActive: Bool](nslayoutconstraint/isactive.md)
  The active state of the constraint.
- [class func deactivate([NSLayoutConstraint])](nslayoutconstraint/deactivate(_:).md)
  Deactivates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/activate(_:))*
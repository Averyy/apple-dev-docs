# deactivate(_:)

**Framework**: AppKit  
**Kind**: method

Deactivates each constraint in the specified array.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func deactivate(_ constraints: [NSLayoutConstraint])
```

#### Discussion

This is a convenience method that provides an easy way to deactivate a set of constraints with one call. The effect of this method is the same as setting the [`isActive`](nslayoutconstraint/isactive.md) property of each constraint to [`false`](https://developer.apple.com/documentation/Swift/false). Typically, using this method is more efficient than deactivating each constraint individually.

## Parameters

- `constraints`: An array of constraints to deactivate.

## See Also

- [var isActive: Bool](nslayoutconstraint/isactive.md)
  The active state of the constraint.
- [class func activate([NSLayoutConstraint])](nslayoutconstraint/activate(_:).md)
  Activates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/deactivate(_:))*
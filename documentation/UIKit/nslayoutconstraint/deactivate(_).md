# deactivate(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Deactivates each constraint in the specified array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func deactivate(_ constraints: [NSLayoutConstraint])
```

```objc
+ (void) deactivateConstraints:(NSArray<NSLayoutConstraint *> *) constraints;
```

## Discussion

This is a convenience method that provides an easy way to deactivate a set of constraints with one call. The effect of this method is the same as setting the [`isActive`](./isactive.md) property of each constraint to [`false`](../../Swift/false.md). Typically, using this method is more efficient than deactivating each constraint individually.

## Parameters

- `constraints`: An array of constraints to deactivate.

## See Also

### Activating and deactivating constraints
- [var isActive: Bool](./isactive.md)
  The active state of the constraint.
- [class func activate([NSLayoutConstraint])](./activate%28_%29.md)
  Activates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/deactivate(_:))*
# activate(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Activates each constraint in the specified array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func activate(_ constraints: [NSLayoutConstraint])
```

```objc
+ (void) activateConstraints:(NSArray<NSLayoutConstraint *> *) constraints;
```

#### Discussion

This convenience method provides an easy way to activate a set of constraints with one call. The effect of this method is the same as setting the [`isActive`](./isactive.md) property of each constraint to [`true`](../../Swift/true.md). Typically, using this method is more efficient than activating each constraint individually.

## Parameters

- `constraints`: An array of constraints to activate.

## See Also

### Activating and deactivating constraints
- [var isActive: Bool](./isactive.md)
  The active state of the constraint.
- [class func deactivate([NSLayoutConstraint])](./deactivate%28_%29.md)
  Deactivates each constraint in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/activate(_:))*
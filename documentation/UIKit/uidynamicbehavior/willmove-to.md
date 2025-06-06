# willMove(to:)

**Framework**: UIKit  
**Kind**: method

Called when the dynamic behavior is added to, or removed from, a dynamic animator.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func willMove(to dynamicAnimator: UIDynamicAnimator?)
```

#### Discussion

Use this method as the override point for responding to changes in the UIKit Dynamics behavior tree that involve the dynamic behavior.

## Parameters

- `dynamicAnimator`: The dynamic animator that the behavior is being added to, or   if being removed from an animator.

## See Also

- [var dynamicAnimator: UIDynamicAnimator?](uidynamicbehavior/dynamicanimator.md)
  The dynamic animator that the dynamic behavior is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/willmove(to:))*
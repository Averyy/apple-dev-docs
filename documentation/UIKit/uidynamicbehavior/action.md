# action

**Framework**: UIKit  
**Kind**: property

The block you want to execute during dynamic animation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var action: (() -> Void)? { get set }
```

#### Discussion

The dynamic animator calls the action block on every animation step.

## See Also

- [func willMove(to: UIDynamicAnimator?)](uidynamicbehavior/willmove(to:).md)
  Called when the dynamic behavior is added to, or removed from, a dynamic animator.
- [func addChildBehavior(UIDynamicBehavior)](uidynamicbehavior/addchildbehavior(_:).md)
  Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [var childBehaviors: [UIDynamicBehavior]](uidynamicbehavior/childbehaviors.md)
  Returns the array of dynamic behaviors that are children of a custom dynamic behavior.
- [func removeChildBehavior(UIDynamicBehavior)](uidynamicbehavior/removechildbehavior(_:).md)
  Removes a child dynamic behavior from a custom dynamic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/action)*
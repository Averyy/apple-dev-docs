# action

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The block you want to execute during dynamic animation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var action: (() -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^action)();
```

#### Discussion

The dynamic animator calls the action block on every animation step.

## See Also

### Related Documentation
- [func willMove(to: UIDynamicAnimator?)](./willmove%28to%29.md)
  Called when the dynamic behavior is added to, or removed from, a dynamic animator.
### Configuring a dynamic behavior
- [func addChildBehavior(UIDynamicBehavior)](./addchildbehavior%28_%29.md)
  Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [var childBehaviors: [UIDynamicBehavior]](./childbehaviors.md)
  Returns the array of dynamic behaviors that are children of a custom dynamic behavior.
- [func removeChildBehavior(UIDynamicBehavior)](./removechildbehavior%28_%29.md)
  Removes a child dynamic behavior from a custom dynamic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/action)*
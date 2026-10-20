# dynamicAnimator

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The dynamic animator that the dynamic behavior is associated with.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var dynamicAnimator: UIDynamicAnimator? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIDynamicAnimator * dynamicAnimator;
```

#### Discussion

If the dynamic behavior is not associated with a dynamic animator, the value of this property is `nil`.

## See Also

### Responding to changes in the behavior tree
- [func willMove(to: UIDynamicAnimator?)](./willmove%28to%29.md)
  Called when the dynamic behavior is added to, or removed from, a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/dynamicanimator)*
# dynamicAnimator

**Framework**: UIKit  
**Kind**: property

The dynamic animator that the dynamic behavior is associated with.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dynamicAnimator: UIDynamicAnimator? { get }
```

#### Discussion

If the dynamic behavior is not associated with a dynamic animator, the value of this property is `nil`.

## See Also

- [func willMove(to: UIDynamicAnimator?)](uidynamicbehavior/willmove(to:).md)
  Called when the dynamic behavior is added to, or removed from, a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/dynamicanimator)*
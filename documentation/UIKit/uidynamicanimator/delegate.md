# delegate

**Framework**: UIKit  
**Kind**: property

The delegate for responding to pausing or resumption of animation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIDynamicAnimatorDelegate)? { get set }
```

#### Discussion

The methods for a dynamic animator delegate are described in [`UIDynamicAnimatorDelegate`](uidynamicanimatordelegate.md).

## See Also

- [protocol UIDynamicAnimatorDelegate](uidynamicanimatordelegate.md)
  To respond to the pausing or resumption of UIKit dynamic animation, configure a custom class to adopt the [`UIDynamicAnimatorDelegate`](uidynamicanimatordelegate.md) protocol. Then, in a dynamic animator (an instance of the [`UIDynamicAnimator`](uidynamicanimator.md) class), set the delegate to be an instance of your custom class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/delegate)*
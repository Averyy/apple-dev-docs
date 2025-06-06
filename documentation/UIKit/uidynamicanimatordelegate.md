# UIDynamicAnimatorDelegate

**Framework**: UIKit  
**Kind**: protocol

To respond to the pausing or resumption of UIKit dynamic animation, configure a custom class to adopt the [`UIDynamicAnimatorDelegate`](uidynamicanimatordelegate.md) protocol. Then, in a dynamic animator (an instance of the [`UIDynamicAnimator`](uidynamicanimator.md) class), set the delegate to be an instance of your custom class.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIDynamicAnimatorDelegate : NSObjectProtocol
```

## Topics

### Responding to animation pausing and resumption
- [func dynamicAnimatorDidPause(UIDynamicAnimator)](uidynamicanimatordelegate/dynamicanimatordidpause(_:).md)
  Called when a dynamic animator pauses the animations for its behaviors’ associated dynamic items.
- [func dynamicAnimatorWillResume(UIDynamicAnimator)](uidynamicanimatordelegate/dynamicanimatorwillresume(_:).md)
  Called when a dynamic animator is about to resume the animations for its behaviors’ associated dynamic items.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIDynamicAnimatorDelegate)?](uidynamicanimator/delegate.md)
  The delegate for responding to pausing or resumption of animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate)*
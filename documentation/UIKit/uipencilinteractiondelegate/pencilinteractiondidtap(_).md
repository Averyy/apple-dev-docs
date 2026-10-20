# pencilInteractionDidTap(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user double-tapped Apple Pencil.

**Availability**:
- iOS 12.1+ - Deprecated in 17.5
- iPadOS 12.1+ - Deprecated in 17.5
- Mac Catalyst 13.1+ - Deprecated in 17.5
- visionOS 1.0+ - Deprecated in 1.2

> **Deprecated**: Use [`pencilInteraction(_:didReceiveTap:)`](./pencilinteraction%28_,didreceivetap%29.md) instead.

## Declaration

```swift
optional func pencilInteractionDidTap(_ interaction: UIPencilInteraction)
```

```objc
- (void) pencilInteractionDidTap:(UIPencilInteraction *) interaction;
```

#### Discussion

When handling the double tap, perform either:

- The action selected by the user in the Settings app, as specified by the [`preferredTapAction`](../uipencilinteraction/preferredtapaction.md) class property.
- An alternative behavior that gives the user the best experience for your app. Should you decide to support an alternative, provide an intuitive way for the user to learn about and enable that behavior.

## See Also

### Handling double-tap interactions
- [func pencilInteraction(UIPencilInteraction, didReceiveTap: UIPencilInteraction.Tap)](./pencilinteraction%28_,didreceivetap%29.md)
  Tells the delegate when a person double-taps Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteractiondidtap(_:))*
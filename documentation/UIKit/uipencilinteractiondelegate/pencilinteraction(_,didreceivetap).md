# pencilInteraction(_:didReceiveTap:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when a person double-taps Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
optional func pencilInteraction(_ interaction: UIPencilInteraction, didReceiveTap tap: UIPencilInteraction.Tap)
```

```objc
- (void) pencilInteraction:(UIPencilInteraction *) interaction didReceiveTap:(UIPencilInteractionTap *) tap;
```

## See Also

### Handling double-tap interactions
- [func pencilInteractionDidTap(UIPencilInteraction)](./pencilinteractiondidtap%28_%29.md)
  Tells the delegate that the user double-tapped Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteraction(_:didreceivetap:))*
# pencilInteractionDidTap(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user double-tapped Apple Pencil.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func pencilInteractionDidTap(_ interaction: UIPencilInteraction)
```

#### Discussion

When handling the double tap, perform either:

- The action selected by the user in the Settings app, as specified by the [`preferredTapAction`](uipencilinteraction/preferredtapaction.md) class property.
- An alternative behavior that gives the user the best experience for your app. Should you decide to support an alternative, provide an intuitive way for the user to learn about and enable that behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteractiondidtap(_:))*
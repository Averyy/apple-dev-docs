# UIEditMenuInteractionAnimating

**Framework**: UIKit  
**Kind**: protocol

Methods adopted by system-supplied animator objects when interacting with menus.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIEditMenuInteractionAnimating : NSObjectProtocol
```

## Topics

### Adding Animations
- [func addAnimations(() -> Void)](uieditmenuinteractionanimating/addanimations(_:).md)
  Adds a closure that performs animations to run alongside the edit menu interaction presentation.
- [func addCompletion(() -> Void)](uieditmenuinteractionanimating/addcompletion(_:).md)
  Adds a closure to perform operations when the edit menu interaction presentation animations are complete.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func editMenuInteraction(UIEditMenuInteraction, menuFor: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu?](uieditmenuinteractiondelegate/editmenuinteraction(_:menufor:suggestedactions:).md)
  Provides the menu to use when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, targetRectFor: UIEditMenuConfiguration) -> CGRect](uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:).md)
  Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, willPresentMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](uieditmenuinteractiondelegate/editmenuinteraction(_:willpresentmenufor:animator:).md)
  Informs the delegate when the interaction is about to present the menu.
- [func editMenuInteraction(UIEditMenuInteraction, willDismissMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](uieditmenuinteractiondelegate/editmenuinteraction(_:willdismissmenufor:animator:).md)
  Informs the delegate when the interaction is about to dismiss the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating)*
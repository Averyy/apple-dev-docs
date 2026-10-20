# UIEditMenuInteractionAnimating

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UIEditMenuInteractionAnimating <NSObject>
```

## Topics

### Adding Animations
- [func addAnimations(() -> Void)](./uieditmenuinteractionanimating/addanimations%28_%29.md)
  Adds a closure that performs animations to run alongside the edit menu interaction presentation.
- [func addCompletion(() -> Void)](./uieditmenuinteractionanimating/addcompletion%28_%29.md)
  Adds a closure to perform operations when the edit menu interaction presentation animations are complete.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the Menu
- [func editMenuInteraction(UIEditMenuInteraction, menuFor: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu?](./uieditmenuinteractiondelegate/editmenuinteraction%28_,menufor,suggestedactions%29.md)
  Provides the menu to use when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, targetRectFor: UIEditMenuConfiguration) -> CGRect](./uieditmenuinteractiondelegate/editmenuinteraction%28_,targetrectfor%29.md)
  Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, willPresentMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](./uieditmenuinteractiondelegate/editmenuinteraction%28_,willpresentmenufor,animator%29.md)
  Informs the delegate when the interaction is about to present the menu.
- [func editMenuInteraction(UIEditMenuInteraction, willDismissMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](./uieditmenuinteractiondelegate/editmenuinteraction%28_,willdismissmenufor,animator%29.md)
  Informs the delegate when the interaction is about to dismiss the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating)*
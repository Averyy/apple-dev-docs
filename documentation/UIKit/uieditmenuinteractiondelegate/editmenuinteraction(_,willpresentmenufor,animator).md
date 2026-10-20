# editMenuInteraction(_:willPresentMenuFor:animator:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the interaction is about to present the menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func editMenuInteraction(_ interaction: UIEditMenuInteraction, willPresentMenuFor configuration: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)
```

```objc
- (void) editMenuInteraction:(UIEditMenuInteraction *) interaction willPresentMenuForConfiguration:(UIEditMenuConfiguration *) configuration animator:(id<UIEditMenuInteractionAnimating>) animator;
```

## Parameters

- `interaction`: The interaction object triggering the menu.
- `configuration`: The object containing the configuration details for the menu.
- `animator`: The object you use to add animations that run alongside the appearance transition.

## See Also

### Customizing the Menu
- [func editMenuInteraction(UIEditMenuInteraction, menuFor: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu?](./editmenuinteraction%28_,menufor,suggestedactions%29.md)
  Provides the menu to use when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, targetRectFor: UIEditMenuConfiguration) -> CGRect](./editmenuinteraction%28_,targetrectfor%29.md)
  Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, willDismissMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](./editmenuinteraction%28_,willdismissmenufor,animator%29.md)
  Informs the delegate when the interaction is about to dismiss the menu.
- [protocol UIEditMenuInteractionAnimating](../uieditmenuinteractionanimating.md)
  Methods adopted by system-supplied animator objects when interacting with menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:willpresentmenufor:animator:))*
# UIEditMenuInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

The methods for customizing the menu the interaction displays.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIEditMenuInteractionDelegate : NSObjectProtocol
```

#### Overview

You use this protocol to customize the actions or presentation of the menu an [`UIEditMenuInteraction`](uieditmenuinteraction.md) object displays.

## Topics

### Customizing the Menu
- [func editMenuInteraction(UIEditMenuInteraction, menuFor: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu?](uieditmenuinteractiondelegate/editmenuinteraction(_:menufor:suggestedactions:).md)
  Provides the menu to use when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, targetRectFor: UIEditMenuConfiguration) -> CGRect](uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:).md)
  Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, willPresentMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](uieditmenuinteractiondelegate/editmenuinteraction(_:willpresentmenufor:animator:).md)
  Informs the delegate when the interaction is about to present the menu.
- [func editMenuInteraction(UIEditMenuInteraction, willDismissMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](uieditmenuinteractiondelegate/editmenuinteraction(_:willdismissmenufor:animator:).md)
  Informs the delegate when the interaction is about to dismiss the menu.
- [protocol UIEditMenuInteractionAnimating](uieditmenuinteractionanimating.md)
  Methods adopted by system-supplied animator objects when interacting with menus.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIEditMenuInteraction](uieditmenuinteraction.md)
  An interaction that provides edit operations using a menu.
- [class UIEditMenuConfiguration](uieditmenuconfiguration.md)
  An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
- [protocol UIResponderStandardEditActions](uiresponderstandardeditactions.md)
  A set of standard methods that apps can adopt to support editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate)*
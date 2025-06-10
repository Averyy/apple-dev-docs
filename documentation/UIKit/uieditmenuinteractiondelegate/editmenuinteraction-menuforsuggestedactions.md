# editMenuInteraction(_:menuFor:suggestedActions:)

**Framework**: UIKit  
**Kind**: method

Provides the menu to use when the interaction begins or requires an update.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func editMenuInteraction(_ interaction: UIEditMenuInteraction, menuFor configuration: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu?
```

#### Return Value

Returns a menu describing the desired menu hierarchy. To present the default system menu, return `nil`. To avoid presenting a menu, return an empty menu.

#### Discussion

UIKit calls this method when the interaction begins or requires an update to the menu’s actions when calling [`reloadVisibleMenu()`](uieditmenuinteraction/reloadvisiblemenu().md). The interaction displays the menu you provide. When not implemented, the default behavior is the same as returning a menu including the suggestedActions.

The following example returns a menu with an additional actions in a submenu.

```swift
func editMenuInteraction(_ interaction: UIEditMenuInteraction, menuFor configuration: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu {
        let indentationMenu = UIMenu(title: "Indentation", image: UIImage(systemName: "list.bullet.indent"), children: [
            UIAction(title: "Increase", image: UIImage(systemName: "increase.indent")) { (action) in
                // Increase indentation action.
                print("increase indent")
            },
            UIAction(title: "Decrease", image: UIImage(systemName: "decrease.indent")) { (action) in
                // Decrease indentation action.
                print("decrease indent")
            }
        ])

        var actions = suggestedActions
        actions.append(indentationMenu)
        return UIMenu(children: actions)
    }
```

## Parameters

- `interaction`: The interaction object triggering the menu.
- `configuration`: The object containing the configuration details for the menu.
- `suggestedActions`: The array of suggested actions UIKit gathers from the   chain. You should include these actions in the menu you return.

## See Also

- [func editMenuInteraction(UIEditMenuInteraction, targetRectFor: UIEditMenuConfiguration) -> CGRect](uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:).md)
  Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [func editMenuInteraction(UIEditMenuInteraction, willPresentMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](uieditmenuinteractiondelegate/editmenuinteraction(_:willpresentmenufor:animator:).md)
  Informs the delegate when the interaction is about to present the menu.
- [func editMenuInteraction(UIEditMenuInteraction, willDismissMenuFor: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)](uieditmenuinteractiondelegate/editmenuinteraction(_:willdismissmenufor:animator:).md)
  Informs the delegate when the interaction is about to dismiss the menu.
- [protocol UIEditMenuInteractionAnimating](uieditmenuinteractionanimating.md)
  Methods adopted by system-supplied animator objects when interacting with menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:menufor:suggestedactions:))*
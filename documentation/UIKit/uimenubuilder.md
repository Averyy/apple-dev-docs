# UIMenuBuilder

**Framework**: UIKit  
**Kind**: protocol

An interface for adding and removing menus from a menu system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIMenuBuilder
```

## Mentions

- [Optimizing your iPad app for Mac](optimizing-your-ipad-app-for-mac.md)

#### Overview

You don’t create a menu builder object. Instead, you override [`buildMenu(with:)`](uiresponder/buildmenu(with:).md) in your app delegate or view controller to receive a builder object. Where you override this method determines the system that the builder updates. To add and remove menus from the menu bar using the [`main`](uimenusystem/main.md) menu system, override [`buildMenu(with:)`](uiresponder/buildmenu(with:).md) in your app delegate. To build a context menu using the [`context`](uimenusystem/context.md) system, override the method in your view controller.

To see an example of how to use a menu builder object, see [`Adding menus and shortcuts to the menu bar and user interface`](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

## Topics

### Getting menu systems and elements
- [var system: UIMenuSystem](uimenubuilder/system.md)
  The menu system that the menu builder modifies.
- [func menu(for: UIMenu.Identifier) -> UIMenu?](uimenubuilder/menu(for:).md)
  Gets the menu for the specified menu identifier.
- [func action(for: UIAction.Identifier) -> UIAction?](uimenubuilder/action(for:).md)
  Gets the action for the specified action identifier.
- [func command(for: Selector, propertyList: Any?) -> UICommand?](uimenubuilder/command(for:propertylist:).md)
  Gets the command for the specified selector and property list.
### Inserting child menus
- [func insertChild(UIMenu, atStartOfMenu: UIMenu.Identifier)](uimenubuilder/insertchild(_:atstartofmenu:).md)
  Adds a child menu as the first element of the specified parent menu.
- [func insertChild(UIMenu, atEndOfMenu: UIMenu.Identifier)](uimenubuilder/insertchild(_:atendofmenu:).md)
  Adds a child menu as the last element of the specified parent menu.
### Inserting sibling menus
- [func insertSibling(UIMenu, beforeMenu: UIMenu.Identifier)](uimenubuilder/insertsibling(_:beforemenu:).md)
  Inserts a sibling menu before the specified menu.
- [func insertSibling(UIMenu, afterMenu: UIMenu.Identifier)](uimenubuilder/insertsibling(_:aftermenu:).md)
  Inserts a sibling menu after the specified menu.
### Replacing menus and child menu elements
- [func replace(menu: UIMenu.Identifier, with: UIMenu)](uimenubuilder/replace(menu:with:).md)
  Replaces the specified menu with a new menu.
- [func replaceChildren(ofMenu: UIMenu.Identifier, from: ([UIMenuElement]) -> [UIMenuElement])](uimenubuilder/replacechildren(ofmenu:from:).md)
  Replaces the elements in a menu with the elements returned by the specified handler block.
### Removing a menu
- [func remove(menu: UIMenu.Identifier)](uimenubuilder/remove(menu:).md)
  Removes a menu from the menu system.

## See Also

- [class UIMenu](uimenu.md)
  A container for grouping related menu elements in an app menu or contextual menu.
- [class UIMenuSystem](uimenusystem.md)
  An object representing a main or contextual menu system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder)*
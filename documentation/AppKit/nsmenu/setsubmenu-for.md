# setSubmenu(_:for:)

**Framework**: AppKit  
**Kind**: method

Assigns a menu to be a submenu of the menu controlled by a given menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSubmenu(_ menu: NSMenu?, for item: NSMenuItem)
```

## Parameters

- `menu`: A menu object that is to be a submenu of the menu.
- `item`: A menu item (that is, an object conforming to the NSMenuItem protocol) that controls `aMenu`. The method sets the action of `anItem` to  [`submenuAction(_:)`](nsmenu/submenuaction(_:).md).

## See Also

- [func submenuAction(Any?)](nsmenu/submenuaction(_:).md)
  The action method assigned to menu items that open submenus.
- [var supermenu: NSMenu?](nsmenu/supermenu.md)
  The parent menu that contains the menu as a submenu.
- [var isTornOff: Bool](nsmenu/istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/setsubmenu(_:for:))*
# submenuAction(_:)

**Framework**: AppKit  
**Kind**: method

The action method assigned to menu items that open submenus.

**Availability**:
- macOS ?+

## Declaration

```swift
func submenuAction(_ sender: Any?)
```

#### Discussion

You may override this method to implement different behavior. Never invoke this method directly.

## See Also

- [func setSubmenu(NSMenu?, for: NSMenuItem)](nsmenu/setsubmenu(_:for:).md)
  Assigns a menu to be a submenu of the menu controlled by a given menu item.
- [var supermenu: NSMenu?](nsmenu/supermenu.md)
  The parent menu that contains the menu as a submenu.
- [var isTornOff: Bool](nsmenu/istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/submenuaction(_:))*
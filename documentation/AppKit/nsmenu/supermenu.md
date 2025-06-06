# supermenu

**Framework**: AppKit  
**Kind**: property

The parent menu that contains the menu as a submenu.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var supermenu: NSMenu? { get set }
```

#### Discussion

This property contains a value of type `NSMenu` representing the the parent menu that contains the menu as a submenu. If the menu has no parent menu, then the value of this property is `nil`.

You should never invoke the setter method for this property directly. The setter method is called automatically when changes to the parent menu occur. You can, however, override the setter method for this property in order to take action when changes to the parent menu occur.

## See Also

- [func setSubmenu(NSMenu?, for: NSMenuItem)](nsmenu/setsubmenu(_:for:).md)
  Assigns a menu to be a submenu of the menu controlled by a given menu item.
- [func submenuAction(Any?)](nsmenu/submenuaction(_:).md)
  The action method assigned to menu items that open submenus.
- [var isTornOff: Bool](nsmenu/istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/supermenu)*
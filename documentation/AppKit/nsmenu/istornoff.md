# isTornOff

**Framework**: AppKit  
**Kind**: property

Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isTornOff: Bool { get }
```

#### Discussion

This property has a value of [`false`](https://developer.apple.com/documentation/Swift/false) if the menu is offscreen, is attached to another menu, or is the main menu. Otherwise, this property has a value of [`true`](https://developer.apple.com/documentation/Swift/true).

##### Special Considerations

This property has no effect in macOS 10.6 and later.

## See Also

- [func setSubmenu(NSMenu?, for: NSMenuItem)](nsmenu/setsubmenu(_:for:).md)
  Assigns a menu to be a submenu of the menu controlled by a given menu item.
- [func submenuAction(Any?)](nsmenu/submenuaction(_:).md)
  The action method assigned to menu items that open submenus.
- [var supermenu: NSMenu?](nsmenu/supermenu.md)
  The parent menu that contains the menu as a submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/istornoff)*
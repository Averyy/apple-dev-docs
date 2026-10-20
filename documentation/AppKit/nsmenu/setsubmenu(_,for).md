# setSubmenu(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Assigns a menu to be a submenu of the menu controlled by a given menu item.

**Availability**:
- macOS

## Declaration

```swift
func setSubmenu(_ menu: NSMenu?, for item: NSMenuItem)
```

```objc
- (void) setSubmenu:(NSMenu *) menu forItem:(NSMenuItem *) item;
```

## Parameters

- `menu`: A menu object that is to be a submenu of the menu.
- `item`: A menu item (that is, an object conforming to the NSMenuItem protocol) that controls `aMenu`. The method sets the action of `anItem` to  [`submenuAction(_:)`](./submenuaction%28_%29.md).

## See Also

### Managing Submenus
- [func submenuAction(Any?)](./submenuaction%28_%29.md)
  The action method assigned to menu items that open submenus.
- [var supermenu: NSMenu?](./supermenu.md)
  The parent menu that contains the menu as a submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/setsubmenu(_:for:))*
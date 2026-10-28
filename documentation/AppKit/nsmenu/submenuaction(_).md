# submenuAction(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The action method assigned to menu items that open submenus.

**Availability**:
- macOS

## Declaration

```swift
func submenuAction(_ sender: Any?)
```

```objc
- (void) submenuAction:(id) sender;
```

## Discussion

You may override this method to implement different behavior. Never invoke this method directly.

## See Also

### Managing Submenus
- [func setSubmenu(NSMenu?, for: NSMenuItem)](./setsubmenu%28_,for%29.md)
  Assigns a menu to be a submenu of the menu controlled by a given menu item.
- [var supermenu: NSMenu?](./supermenu.md)
  The parent menu that contains the menu as a submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/submenuaction(_:))*
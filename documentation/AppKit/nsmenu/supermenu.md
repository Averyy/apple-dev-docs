# supermenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The parent menu that contains the menu as a submenu.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var supermenu: NSMenu? { get set }
```

```objc
@property (assign, nullable) NSMenu * supermenu;
```

## Discussion

This property contains a value of type `NSMenu` representing the the parent menu that contains the menu as a submenu. If the menu has no parent menu, then the value of this property is `nil`.

You should never invoke the setter method for this property directly. The setter method is called automatically when changes to the parent menu occur. You can, however, override the setter method for this property in order to take action when changes to the parent menu occur.

## See Also

### Managing Submenus
- [func setSubmenu(NSMenu?, for: NSMenuItem)](./setsubmenu%28_,for%29.md)
  Assigns a menu to be a submenu of the menu controlled by a given menu item.
- [func submenuAction(Any?)](./submenuaction%28_%29.md)
  The action method assigned to menu items that open submenus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/supermenu)*
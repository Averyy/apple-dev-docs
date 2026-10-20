# submenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The submenu of the menu item.

**Availability**:
- macOS

## Declaration

```swift
var submenu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * submenu;
```

#### Discussion

The default implementation of the `NSMenuItem` class raises an exception if `aSubmenu` already has a supermenu.

## See Also

### Managing submenus
- [var hasSubmenu: Bool](./hassubmenu.md)
  A Boolean value that indicates whether the menu item has a submenu.
- [var parent: NSMenuItem?](./parent.md)
  The menu item whose submenu contains the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/submenu)*
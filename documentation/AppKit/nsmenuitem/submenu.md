# submenu

**Framework**: AppKit  
**Kind**: property

The submenu of the menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
var submenu: NSMenu? { get set }
```

#### Discussion

The default implementation of the `NSMenuItem` class raises an exception if `aSubmenu` already has a supermenu.

## See Also

- [var hasSubmenu: Bool](nsmenuitem/hassubmenu.md)
  A Boolean value that indicates whether the menu item has a submenu.
- [var parent: NSMenuItem?](nsmenuitem/parent.md)
  The menu item whose submenu contains the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/submenu)*
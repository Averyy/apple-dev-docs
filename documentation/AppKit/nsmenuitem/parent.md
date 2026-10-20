# parent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item whose submenu contains the receiver.

**Availability**:
- macOS 10.6+

## Declaration

```swift
unowned(unsafe) var parent: NSMenuItem? { get }
```

```objc
@property (assign, readonly, nullable) NSMenuItem * parentItem;
```

## See Also

### Managing submenus
- [var submenu: NSMenu?](./submenu.md)
  The submenu of the menu item.
- [var hasSubmenu: Bool](./hassubmenu.md)
  A Boolean value that indicates whether the menu item has a submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/parent)*
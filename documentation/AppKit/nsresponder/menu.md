# menu

**Framework**: AppKit  
**Kind**: property

Returns the responder’s menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var menu: NSMenu? { get set }
```

#### Discussion

For `NSApplication` this menu is the same as the menu returned by its [`mainMenu`](nsapplication/mainmenu.md) property.

## See Also

- [class var defaultMenu: NSMenu?](nsview/defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func menu(for: NSEvent) -> NSMenu?](nsview/menu(for:).md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/menu)*
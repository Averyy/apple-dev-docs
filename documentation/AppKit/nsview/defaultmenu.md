# defaultMenu

**Framework**: AppKit  
**Kind**: property

Overridden by subclasses to return the default pop-up menu for instances of the receiving class.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var defaultMenu: NSMenu? { get }
```

#### Discussion

The default implementation returns `nil`.

## See Also

- [var menu: NSMenu?](nsresponder/menu.md)
  Returns the responder’s menu.
- [func menu(for: NSEvent) -> NSMenu?](nsview/menu(for:).md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.
- [func willOpenMenu(NSMenu, with: NSEvent)](nsview/willopenmenu(_:with:).md)
  Called just before a contextual menu for a view is opened on screen.
- [func didCloseMenu(NSMenu, with: NSEvent?)](nsview/didclosemenu(_:with:).md)
  Called after a contextual menu that was displayed from the receiving view has been closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/defaultmenu)*
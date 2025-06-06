# didCloseMenu(_:with:)

**Framework**: AppKit  
**Kind**: method

Called after a contextual menu that was displayed from the receiving view has been closed.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func didCloseMenu(_ menu: NSMenu, with event: NSEvent?)
```

#### Discussion

This method is called only if the contextual menu had been opened and the view has previously received the [`willOpenMenu(_:with:)`](nsview/willopenmenu(_:with:).md) method. When the view receives [`didCloseMenu(_:with:)`](nsview/didclosemenu(_:with:).md), it should reset its visual state, if necessary. For example, if a table view selected a row in response to a contextual menu being displayed, this method could deselect the row.

## Parameters

- `menu`: The menu that was closed.
- `event`: The event that caused the menu to close, if there was one. If an event did not cause the menu to close, this value is  .

## See Also

- [func menu(for: NSEvent) -> NSMenu?](nsview/menu(for:).md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.
- [class var defaultMenu: NSMenu?](nsview/defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func willOpenMenu(NSMenu, with: NSEvent)](nsview/willopenmenu(_:with:).md)
  Called just before a contextual menu for a view is opened on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/didclosemenu(_:with:))*
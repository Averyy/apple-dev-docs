# didCloseMenu(_:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called after a contextual menu that was displayed from the receiving view has been closed.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func didCloseMenu(_ menu: NSMenu, with event: NSEvent?)
```

```objc
- (void) didCloseMenu:(NSMenu *) menu withEvent:(NSEvent *) event;
```

#### Discussion

This method is called only if the contextual menu had been opened and the view has previously received the [`willOpenMenu(_:with:)`](./willopenmenu%28_,with%29.md) method. When the view receives [`didCloseMenu(_:with:)`](./didclosemenu%28_,with%29.md), it should reset its visual state, if necessary. For example, if a table view selected a row in response to a contextual menu being displayed, this method could deselect the row.

## Parameters

- `menu`: The menu that was closed.
- `event`: The event that caused the menu to close, if there was one. If an event did not cause the menu to close, this value is `nil`.

## See Also

### Managing Contextual Menus
- [func menu(for: NSEvent) -> NSMenu?](./menu%28for%29.md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.
- [class var defaultMenu: NSMenu?](./defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func willOpenMenu(NSMenu, with: NSEvent)](./willopenmenu%28_,with%29.md)
  Called just before a contextual menu for a view is opened on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/didclosemenu(_:with:))*
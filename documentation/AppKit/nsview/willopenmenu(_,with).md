# willOpenMenu(_:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called just before a contextual menu for a view is opened on screen.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func willOpenMenu(_ menu: NSMenu, with event: NSEvent)
```

```objc
- (void) willOpenMenu:(NSMenu *) menu withEvent:(NSEvent *) event;
```

## Discussion

This method is called just before a contextual menu for a view is opened on screen. It provides an opportunity to make any desired changes to the visual state of the view. For example, a table view might select a row in response to the contextual menu being displayed.

## Parameters

- `menu`: The menu that will be opened.
- `event`: The event that caused the menu to open.

## See Also

### Managing Contextual Menus
- [func menu(for: NSEvent) -> NSMenu?](./menu%28for%29.md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.
- [class var defaultMenu: NSMenu?](./defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func didCloseMenu(NSMenu, with: NSEvent?)](./didclosemenu%28_,with%29.md)
  Called after a contextual menu that was displayed from the receiving view has been closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/willopenmenu(_:with:))*
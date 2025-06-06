# menu(for:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func menu(for event: NSEvent) -> NSMenu?
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)

#### Discussion

The view can use information in the mouse event, such as its location over a particular element of the view, to determine what kind of menu to return. For example, a text object might display a text-editing menu when the cursor lies over text and a menu for changing graphics attributes when the cursor lies over an embedded image.

The default implementation returns the view’s normal menu.

## Parameters

- `event`: An object representing a mouse-down event.

## See Also

- [var menu: NSMenu?](nsresponder/menu.md)
  Returns the responder’s menu.
- [class var defaultMenu: NSMenu?](nsview/defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func willOpenMenu(NSMenu, with: NSEvent)](nsview/willopenmenu(_:with:).md)
  Called just before a contextual menu for a view is opened on screen.
- [func didCloseMenu(NSMenu, with: NSEvent?)](nsview/didclosemenu(_:with:).md)
  Called after a contextual menu that was displayed from the receiving view has been closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/menu(for:))*
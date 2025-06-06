# popUpContextMenu(_:with:for:)

**Framework**: AppKit  
**Kind**: method

Displays a contextual menu over a view for an event.

**Availability**:
- macOS ?+

## Declaration

```swift
class func popUpContextMenu(_ menu: NSMenu, with event: NSEvent, for view: NSView)
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)

## Parameters

- `menu`: The menu object to use for the contextual menu.
- `event`: An   object representing the event.
- `view`: The view object over which to display the contextual menu.

## See Also

- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView, with: NSFont?)](nsmenu/popupcontextmenu(_:with:for:with:).md)
  Displays a contextual menu over a view for an event using a specified font.
- [func helpRequested(with: NSEvent)](nsmenu/helprequested(with:).md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [func popUp(positioning: NSMenuItem?, at: NSPoint, in: NSView?) -> Bool](nsmenu/popup(positioning:at:in:).md)
  Pops up the menu at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:))*
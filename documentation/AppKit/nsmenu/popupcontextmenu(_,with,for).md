# popUpContextMenu(_:with:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Displays a contextual menu over a view for an event.

**Availability**:
- macOS

## Declaration

```swift
class func popUpContextMenu(_ menu: NSMenu, with event: NSEvent, for view: NSView)
```

```objc
+ (void) popUpContextMenu:(NSMenu *) menu withEvent:(NSEvent *) event forView:(NSView *) view;
```

## Mentions

- [Supporting Continuity Camera in Your Mac App](../supporting-continuity-camera-in-your-mac-app.md)
- [Supporting Writing Tools via the pasteboard](../supporting-writing-tools-via-the-pasteboard.md)

## Parameters

- `menu`: The menu object to use for the contextual menu.
- `event`: An [`NSEvent`](../nsevent.md) object representing the event.
- `view`: The view object over which to display the contextual menu.

## See Also

### Displaying Context-Sensitive Help
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView, with: NSFont?)](./popupcontextmenu%28_,with,for,with%29.md)
  Displays a contextual menu over a view for an event using a specified font.
- [func popUp(positioning: NSMenuItem?, at: NSPoint, in: NSView?) -> Bool](./popup%28positioning,at,in%29.md)
  Pops up the menu at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:))*
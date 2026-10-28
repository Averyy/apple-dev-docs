# popUp(positioning:at:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Pops up the menu at the specified location.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func popUp(positioning item: NSMenuItem?, at location: NSPoint, in view: NSView?) -> Bool
```

```objc
- (BOOL) popUpMenuPositioningItem:(NSMenuItem *) item atLocation:(NSPoint) location inView:(NSView *) view;
```

## Return Value

[`true`](../../Swift/true.md) if menu tracking ended because an item was selected, and [`false`](../../Swift/false.md) if menu tracking was cancelled for any reason.

## Discussion

Displays the menu as a pop-up menu. The top left corner of the specified item (if specified, `item` must be present in the menu) is positioned at the specified location in the specified view, interpreted in the view’s own coordinate system.

If `item` is `nil`, the menu is positioned such that the top left of the menu content frame is at the given location.

If `view` is `nil`, the location is interpreted in the screen coordinate system. This allows you to pop up a menu disconnected from any window.

## Parameters

- `item`: The menu item to be positioned at the specified location in the view.
- `location`: The location in the `view` coordinate system to display the menu item.
- `view`: The view to display the menu item over.

## See Also

### Displaying Context-Sensitive Help
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView)](./popupcontextmenu%28_,with,for%29.md)
  Displays a contextual menu over a view for an event.
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView, with: NSFont?)](./popupcontextmenu%28_,with,for,with%29.md)
  Displays a contextual menu over a view for an event using a specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/popup(positioning:at:in:))*
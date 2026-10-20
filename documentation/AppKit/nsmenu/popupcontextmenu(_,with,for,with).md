# popUpContextMenu(_:with:for:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Displays a contextual menu over a view for an event using a specified font.

**Availability**:
- macOS

## Declaration

```swift
class func popUpContextMenu(_ menu: NSMenu, with event: NSEvent, for view: NSView, with font: NSFont?)
```

```objc
+ (void) popUpContextMenu:(NSMenu *) menu withEvent:(NSEvent *) event forView:(NSView *) view withFont:(NSFont *) font;
```

#### Discussion

Specifying a font using the font parameter is discouraged. Instead, set the menu’s font using the [`font`](./font.md) property, then pass `nil` for the `font` parameter.

## Parameters

- `menu`: The menu object to use for the contextual menu.
- `event`: An [`NSEvent`](../nsevent.md) object representing the event.
- `view`: The view object over which to display the contextual menu.
- `font`: An [`NSFont`](../nsfont.md) object representing the font for the contextual menu. If you pass in `nil` for the font, the method uses the default font for `menu`.

## See Also

### Displaying Context-Sensitive Help
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView)](./popupcontextmenu%28_,with,for%29.md)
  Displays a contextual menu over a view for an event.
- [func popUp(positioning: NSMenuItem?, at: NSPoint, in: NSView?) -> Bool](./popup%28positioning,at,in%29.md)
  Pops up the menu at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:with:))*
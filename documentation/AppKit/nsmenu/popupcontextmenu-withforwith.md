# popUpContextMenu(_:with:for:with:)

**Framework**: AppKit  
**Kind**: method

Displays a contextual menu over a view for an event using a specified font.

**Availability**:
- macOS ?+

## Declaration

```swift
class func popUpContextMenu(_ menu: NSMenu, with event: NSEvent, for view: NSView, with font: NSFont?)
```

#### Discussion

Specifying a font using the font parameter is discouraged. Instead, set the menu’s font using the [`font`](nsmenu/font.md) property, then pass `nil` for the `font` parameter.

## Parameters

- `menu`: The menu object to use for the contextual menu.
- `event`: An   object representing the event.
- `view`: The view object over which to display the contextual menu.
- `font`: An   object representing the font for the contextual menu. If you pass in   for the font, the method uses the default font for  .

## See Also

- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView)](nsmenu/popupcontextmenu(_:with:for:).md)
  Displays a contextual menu over a view for an event.
- [func helpRequested(with: NSEvent)](nsmenu/helprequested(with:).md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [func popUp(positioning: NSMenuItem?, at: NSPoint, in: NSView?) -> Bool](nsmenu/popup(positioning:at:in:).md)
  Pops up the menu at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:with:))*
# helpRequested(with:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to implement specialized context-sensitive help behavior.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func helpRequested(with eventPtr: NSEvent)
```

#### Discussion

Subclasses in their implementation of this method should cause the Help Manager ([`NSHelpManager`](nshelpmanager.md)) to display the help associated with the menu. Never invoke this method directly.

##### Special Considerations

In macOS 10.6 and later this method has no effect. This method may be deprecated in a future release.

## Parameters

- `eventPtr`: An   object representing the event associated with the help request.

## See Also

- [func showContextHelp(for: Any, locationHint: NSPoint) -> Bool](nshelpmanager/showcontexthelp(for:locationhint:).md)
  Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView)](nsmenu/popupcontextmenu(_:with:for:).md)
  Displays a contextual menu over a view for an event.
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView, with: NSFont?)](nsmenu/popupcontextmenu(_:with:for:with:).md)
  Displays a contextual menu over a view for an event using a specified font.
- [func popUp(positioning: NSMenuItem?, at: NSPoint, in: NSView?) -> Bool](nsmenu/popup(positioning:at:in:).md)
  Pops up the menu at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/helprequested(with:))*
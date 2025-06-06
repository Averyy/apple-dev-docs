# buttonNumber

**Framework**: AppKit  
**Kind**: property

The button number for a mouse event.

**Availability**:
- macOS ?+

## Declaration

```swift
var buttonNumber: Int { get }
```

#### Discussion

This property is intended for use with the `NSOtherMouseDown`, `NSOtherMouseUp`, and `NSOtherMouseDragged` events, but will return values for `NSLeftMouse...` and `NSRightMouse...` events also. If this event is not a mouse event, the property is set to `0`.

## See Also

- [class var pressedMouseButtons: Int](nsevent/pressedmousebuttons.md)
  The indices of the currently pressed mouse buttons.
- [class var doubleClickInterval: TimeInterval](nsevent/doubleclickinterval.md)
  The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.
- [class var mouseLocation: NSPoint](nsevent/mouselocation.md)
  Reports the current mouse position in screen coordinates.
- [var clickCount: Int](nsevent/clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var associatedEventsMask: NSEvent.EventTypeMask](nsevent/associatedeventsmask.md)
  The associated events mask of a mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/buttonnumber)*
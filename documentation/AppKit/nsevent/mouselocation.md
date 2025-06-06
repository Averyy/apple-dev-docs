# mouseLocation

**Framework**: AppKit  
**Kind**: property

Reports the current mouse position in screen coordinates.

**Availability**:
- macOS ?+

## Declaration

```swift
class var mouseLocation: NSPoint { get }
```

#### Return Value

The current mouse location in screen coordinates.

#### Discussion

This method is similar to the [`mouseLocationOutsideOfEventStream`](nswindow/mouselocationoutsideofeventstream.md) method of [`NSWindow`](nswindow.md). It returns the location regardless of the current event or pending events. The difference between these methods is that [`mouseLocationOutsideOfEventStream`](nswindow/mouselocationoutsideofeventstream.md) returns a point in the receiving window’s coordinates, and [`mouseLocation`](nsevent/mouselocation.md) returns the same information in screen coordinates.

## See Also

- [class var pressedMouseButtons: Int](nsevent/pressedmousebuttons.md)
  The indices of the currently pressed mouse buttons.
- [class var doubleClickInterval: TimeInterval](nsevent/doubleclickinterval.md)
  The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.
- [var buttonNumber: Int](nsevent/buttonnumber.md)
  The button number for a mouse event.
- [var clickCount: Int](nsevent/clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var associatedEventsMask: NSEvent.EventTypeMask](nsevent/associatedeventsmask.md)
  The associated events mask of a mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/mouselocation)*
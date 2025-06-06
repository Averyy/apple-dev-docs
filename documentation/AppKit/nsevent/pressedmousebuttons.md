# pressedMouseButtons

**Framework**: AppKit  
**Kind**: property

The indices of the currently pressed mouse buttons.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var pressedMouseButtons: Int { get }
```

#### Return Value

The indices of the currently depressed mouse buttons.

#### Discussion

A return value of `1 << 0` corresponds to the left mouse button, `1 << 1` corresponds to the right mouse button, `1<< n`, `n >=2` correspond to other mouse buttons.

This returns the state of devices combined with synthesized events at the moment, independent of which events have been delivered via the event stream, so this method is not suitable for tracking.

## See Also

- [class var doubleClickInterval: TimeInterval](nsevent/doubleclickinterval.md)
  The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.
- [class var mouseLocation: NSPoint](nsevent/mouselocation.md)
  Reports the current mouse position in screen coordinates.
- [var buttonNumber: Int](nsevent/buttonnumber.md)
  The button number for a mouse event.
- [var clickCount: Int](nsevent/clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var associatedEventsMask: NSEvent.EventTypeMask](nsevent/associatedeventsmask.md)
  The associated events mask of a mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pressedmousebuttons)*
# doubleClickInterval

**Framework**: AppKit  
**Kind**: property

The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var doubleClickInterval: TimeInterval { get }
```

#### Return Value

The double-click time interval, in seconds.

#### Discussion

This is a system setting. You can’t change the value by overriding this method.

## See Also

- [class var pressedMouseButtons: Int](nsevent/pressedmousebuttons.md)
  The indices of the currently pressed mouse buttons.
- [class var mouseLocation: NSPoint](nsevent/mouselocation.md)
  Reports the current mouse position in screen coordinates.
- [var buttonNumber: Int](nsevent/buttonnumber.md)
  The button number for a mouse event.
- [var clickCount: Int](nsevent/clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var associatedEventsMask: NSEvent.EventTypeMask](nsevent/associatedeventsmask.md)
  The associated events mask of a mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/doubleclickinterval)*
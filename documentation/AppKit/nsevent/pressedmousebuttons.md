# pressedMouseButtons

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The indices of the currently pressed mouse buttons.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var pressedMouseButtons: Int { get }
```

```objc
@property (class, readonly) NSUInteger pressedMouseButtons;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Return Value

The indices of the currently depressed mouse buttons.

## Discussion

A return value of `1 << 0` corresponds to the left mouse button, `1 << 1` corresponds to the right mouse button, `1<< n`, `n >=2` correspond to other mouse buttons.

This returns the state of devices combined with synthesized events at the moment, independent of which events have been delivered via the event stream, so this method is not suitable for tracking.

## See Also

### Getting mouse event information
- [class var doubleClickInterval: TimeInterval](./doubleclickinterval.md)
  The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.
- [class var mouseLocation: NSPoint](./mouselocation.md)
  Reports the current mouse position in screen coordinates.
- [var buttonNumber: Int](./buttonnumber.md)
  The button number for a mouse event.
- [var clickCount: Int](./clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var associatedEventsMask: NSEvent.EventTypeMask](./associatedeventsmask.md)
  The associated events mask of a mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pressedmousebuttons)*
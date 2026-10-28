# clickCount

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of mouse clicks associated with a mouse-down or mouse-up event.

**Availability**:
- macOS

## Declaration

```swift
var clickCount: Int { get }
```

```objc
@property (readonly) NSInteger clickCount;
```

## Discussion

Raises an `NSInternalInconsistencyException` if accessed on a non-mouse event.

This property is set to `0` for a mouse-up event if a time threshold has passed since the corresponding mouse-down event. This is because if this time threshold passes before the mouse button is released, it is no longer considered a mouse click, but a mouse-down event followed by a mouse-up event.

The return value of this method is meaningless for events other than mouse-down or mouse-up events.

## See Also

### Related Documentation
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](./mouseevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,clickcount,pressure%29.md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
### Getting mouse event information
- [class var pressedMouseButtons: Int](./pressedmousebuttons.md)
  The indices of the currently pressed mouse buttons.
- [class var doubleClickInterval: TimeInterval](./doubleclickinterval.md)
  The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.
- [class var mouseLocation: NSPoint](./mouselocation.md)
  Reports the current mouse position in screen coordinates.
- [var buttonNumber: Int](./buttonnumber.md)
  The button number for a mouse event.
- [var associatedEventsMask: NSEvent.EventTypeMask](./associatedeventsmask.md)
  The associated events mask of a mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/clickcount)*
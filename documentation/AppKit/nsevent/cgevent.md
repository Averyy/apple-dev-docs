# cgEvent

**Framework**: AppKit  
**Kind**: property

The Core Graphics event object corresponding to this event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var cgEvent: CGEvent? { get }
```

#### Discussion

The [`CGEvent`](https://developer.apple.com/documentation/CoreGraphics/CGEvent) opaque type returned is autoreleased. If no `CGEventRef` object corresponding to the `NSEvent` object can be created, this method returns `NULL`.

## See Also

- [init?(cgEvent: CGEvent)](nsevent/init(cgevent:).md)
  Creates and returns an event object for a Core Graphics event.
- [var locationInWindow: NSPoint](nsevent/locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var timestamp: TimeInterval](nsevent/timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var window: NSWindow?](nsevent/window.md)
  The window object associated with the event.
- [var windowNumber: Int](nsevent/windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](nsevent/eventref.md)
  An opaque Carbon type associated with this event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/cgevent)*
# timestamp

**Framework**: AppKit  
**Kind**: property

The time when the event occurred in seconds since system startup.

**Availability**:
- macOS ?+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

## See Also

- [var systemUptime: TimeInterval](../Foundation/ProcessInfo/systemUptime.md)
  The amount of time the system has been awake since the last time it was restarted.
- [var locationInWindow: NSPoint](nsevent/locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var window: NSWindow?](nsevent/window.md)
  The window object associated with the event.
- [var windowNumber: Int](nsevent/windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](nsevent/eventref.md)
  An opaque Carbon type associated with this event.
- [var cgEvent: CGEvent?](nsevent/cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/timestamp)*
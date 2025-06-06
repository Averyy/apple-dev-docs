# eventRef

**Framework**: AppKit  
**Kind**: property

An opaque Carbon type associated with this event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var eventRef: UnsafeRawPointer? { get }
```

#### Discussion

This method is valid for all types of events. The `EventRef` object is retained by the receiver, so it is valid as long as the `NSEvent` object is valid, and is released when the `NSEvent` object is freed. You can use `RetainEvent(_:)` to extend the lifetime of the `EventRef` object, with a corresponding `ReleaseEvent(_:)` when you are done with it.

The system typically creates user-input events with an associated `EventRef`. Other `NSEvent` objects create an `EventRef` when this property is first accessed, if possible. If there is no equivalent `NSEvent` for this event, the property is set to `NULL`.

## See Also

- [init?(eventRef: UnsafeRawPointer)](nsevent/init(eventref:).md)
  Creates and returns a new event object for a Carbon event.
- [var locationInWindow: NSPoint](nsevent/locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var timestamp: TimeInterval](nsevent/timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var window: NSWindow?](nsevent/window.md)
  The window object associated with the event.
- [var windowNumber: Int](nsevent/windownumber.md)
  The identifier for the window device associated with the event.
- [var cgEvent: CGEvent?](nsevent/cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventref)*
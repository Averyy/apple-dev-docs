# tabletPoint(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that a tablet-point event has occurred.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tabletPoint(with event: NSEvent)
```

#### Discussion

Tablet events are represented by `NSEvent` objects of type [`NSTabletPoint`](nstabletpoint.md). They describe the current state of a transducer (that is, a pointing device) that is in proximity to its tablet, reflecting changes such as location, pressure, tilt, and rotation. See the [`NSEvent`](nsevent.md) reference for the methods that allow you to extract this and other information from `event`. The default implementation of `NSResponder` passes the message to the next responder.

## Parameters

- `event`: An object encapsulating information about the tablet-point event.

## See Also

- [func cursorUpdate(with: NSEvent)](nsresponder/cursorupdate(with:).md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func flagsChanged(with: NSEvent)](nsresponder/flagschanged(with:).md)
  Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).
- [func tabletProximity(with: NSEvent)](nsresponder/tabletproximity(with:).md)
  Informs the receiver that a tablet-proximity event has occurred.
- [func helpRequested(NSEvent)](nsresponder/helprequested(_:).md)
  Displays context-sensitive help for the receiver if help has been registered.
- [func scrollWheel(with: NSEvent)](nsresponder/scrollwheel(with:).md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func quickLook(with: NSEvent)](nsresponder/quicklook(with:).md)
  Performs a Quick Look on the content at the location specified by the supplied event.
- [func changeMode(with: NSEvent)](nsresponder/changemode(with:).md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/tabletpoint(with:))*
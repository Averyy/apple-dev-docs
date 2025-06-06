# tabletProximity(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that a tablet-proximity event has occurred.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tabletProximity(with event: NSEvent)
```

#### Discussion

Tablet events are represented by `NSEvent` objects of type [`NSTabletProximity`](nstabletproximity.md). Tablet devices generate proximity events when the transducer (pointing device) nears a tablet and when it moves away from a tablet. From an event object of this type you can extract information about the kind of device and its capabilities, as well as the relation of this tablet-proximity event to various tablet-point events; see the [`NSEvent`](nsevent.md) reference for details. The default implementation passes the message to the next responder.

## Parameters

- `event`: An object encapsulating information about the tablet-point event.

## See Also

- [func cursorUpdate(with: NSEvent)](nsresponder/cursorupdate(with:).md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func flagsChanged(with: NSEvent)](nsresponder/flagschanged(with:).md)
  Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).
- [func tabletPoint(with: NSEvent)](nsresponder/tabletpoint(with:).md)
  Informs the receiver that a tablet-point event has occurred.
- [func helpRequested(NSEvent)](nsresponder/helprequested(_:).md)
  Displays context-sensitive help for the receiver if help has been registered.
- [func scrollWheel(with: NSEvent)](nsresponder/scrollwheel(with:).md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func quickLook(with: NSEvent)](nsresponder/quicklook(with:).md)
  Performs a Quick Look on the content at the location specified by the supplied event.
- [func changeMode(with: NSEvent)](nsresponder/changemode(with:).md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/tabletproximity(with:))*
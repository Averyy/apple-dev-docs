# changeMode(with:)

**Framework**: AppKit  
**Kind**: method

Informs the responder that performed a double-tap on the side of an Apple Pencil.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
func changeMode(with event: NSEvent)
```

#### Discussion

The default implementation passes the event to the next responder.

## Parameters

- `event`: An object encapsulating information about the change-mode event.

## See Also

- [func cursorUpdate(with: NSEvent)](nsresponder/cursorupdate(with:).md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func flagsChanged(with: NSEvent)](nsresponder/flagschanged(with:).md)
  Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).
- [func tabletPoint(with: NSEvent)](nsresponder/tabletpoint(with:).md)
  Informs the receiver that a tablet-point event has occurred.
- [func tabletProximity(with: NSEvent)](nsresponder/tabletproximity(with:).md)
  Informs the receiver that a tablet-proximity event has occurred.
- [func helpRequested(NSEvent)](nsresponder/helprequested(_:).md)
  Displays context-sensitive help for the receiver if help has been registered.
- [func scrollWheel(with: NSEvent)](nsresponder/scrollwheel(with:).md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func quickLook(with: NSEvent)](nsresponder/quicklook(with:).md)
  Performs a Quick Look on the content at the location specified by the supplied event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/changemode(with:))*
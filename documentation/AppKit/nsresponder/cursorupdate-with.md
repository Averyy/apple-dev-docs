# cursorUpdate(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the mouse cursor has moved into a cursor rectangle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func cursorUpdate(with event: NSEvent)
```

#### Discussion

Override this method to set the cursor image. The default implementation uses cursor rectangles, if cursor rectangles are currently valid.  If they are not, it calls `super` to send the message up the responder chain.

If the responder implements this method, but decides not to handle a particular event, it should invoke the superclass implementation of this method.

## Parameters

- `event`: An object encapsulating information about the cursor-update event ( ).

## See Also

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
- [func changeMode(with: NSEvent)](nsresponder/changemode(with:).md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/cursorupdate(with:))*
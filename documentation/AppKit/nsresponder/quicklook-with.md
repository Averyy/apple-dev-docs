# quickLook(with:)

**Framework**: AppKit  
**Kind**: method

Performs a Quick Look on the content at the location specified by the supplied event.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func quickLook(with event: NSEvent)
```

#### Discussion

The [`NSEvent.EventType.quickLook`](nsevent/eventtype/quicklook.md) event type supports this method. The only valid properties of an [`NSEvent.EventType.quickLook`](nsevent/eventtype/quicklook.md) event are [`locationInWindow`](nsevent/locationinwindow.md) and [`modifierFlags`](nsevent/modifierflags-swift.property.md). A Quick Look event does not come in through the normal event mechanism; therefore, there is no corresponding event mask for it, nor should you attempt to look for it in a [`sendEvent(_:)`](nswindow/sendevent(_:).md) message or with the [`nextEvent(matching:)`](nswindow/nextevent(matching:).md) methods.

If there are no Quick Look items at the location, call super.

`NSResponder` declares but doesn’t implement this method.

## Parameters

- `event`: An event object containing the location of the Quick Look content.

## See Also

- [NSEvent.EventType.quickLook](nsevent/eventtype/quicklook.md)
  An event that initiates a Quick Look request.
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
- [func changeMode(with: NSEvent)](nsresponder/changemode(with:).md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/quicklook(with:))*
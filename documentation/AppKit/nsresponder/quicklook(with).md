# quickLook(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs a Quick Look on the content at the location specified by the supplied event.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func quickLook(with event: NSEvent)
```

```objc
- (void) quickLookWithEvent:(NSEvent *) event;
```

## Discussion

The [`NSEvent.EventType.quickLook`](../nsevent/eventtype/quicklook.md) event type supports this method. The only valid properties of an [`NSEvent.EventType.quickLook`](../nsevent/eventtype/quicklook.md) event are [`locationInWindow`](../nsevent/locationinwindow.md) and [`modifierFlags`](../nsevent/modifierflags-swift.property.md). A Quick Look event does not come in through the normal event mechanism; therefore, there is no corresponding event mask for it, nor should you attempt to look for it in a [`sendEvent(_:)`](../nswindow/sendevent%28_%29.md) message or with the [`nextEvent(matching:)`](../nswindow/nextevent%28matching%29.md) methods.

If there are no Quick Look items at the location, call super.

`NSResponder` declares but doesn’t implement this method.

## Parameters

- `event`: An event object containing the location of the Quick Look content.

## See Also

### Related Documentation
- [NSEvent.EventType.quickLook](../nsevent/eventtype/quicklook.md)
  An event that initiates a Quick Look request.
### Responding to Other Kinds of Events
- [func cursorUpdate(with: NSEvent)](./cursorupdate%28with%29.md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func flagsChanged(with: NSEvent)](./flagschanged%28with%29.md)
  Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).
- [func tabletPoint(with: NSEvent)](./tabletpoint%28with%29.md)
  Informs the receiver that a tablet-point event has occurred.
- [func tabletProximity(with: NSEvent)](./tabletproximity%28with%29.md)
  Informs the receiver that a tablet-proximity event has occurred.
- [func helpRequested(NSEvent)](./helprequested%28_%29.md)
  Displays context-sensitive help for the receiver if help has been registered.
- [func scrollWheel(with: NSEvent)](./scrollwheel%28with%29.md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func changeMode(with: NSEvent)](./changemode%28with%29.md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/quicklook(with:))*
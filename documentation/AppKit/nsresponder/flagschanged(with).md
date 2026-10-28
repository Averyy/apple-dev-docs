# flagsChanged(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).

**Availability**:
- macOS

## Declaration

```swift
func flagsChanged(with event: NSEvent)
```

```objc
- (void) flagsChanged:(NSEvent *) event;
```

## Discussion

The default implementation simply passes this message to the next responder.

## Parameters

- `event`: An object encapsulating information about the modifier-key event.

## See Also

### Responding to Other Kinds of Events
- [func cursorUpdate(with: NSEvent)](./cursorupdate%28with%29.md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func tabletPoint(with: NSEvent)](./tabletpoint%28with%29.md)
  Informs the receiver that a tablet-point event has occurred.
- [func tabletProximity(with: NSEvent)](./tabletproximity%28with%29.md)
  Informs the receiver that a tablet-proximity event has occurred.
- [func helpRequested(NSEvent)](./helprequested%28_%29.md)
  Displays context-sensitive help for the receiver if help has been registered.
- [func scrollWheel(with: NSEvent)](./scrollwheel%28with%29.md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func quickLook(with: NSEvent)](./quicklook%28with%29.md)
  Performs a Quick Look on the content at the location specified by the supplied event.
- [func changeMode(with: NSEvent)](./changemode%28with%29.md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/flagschanged(with:))*
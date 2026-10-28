# changeMode(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the responder that performed a double-tap on the side of an Apple Pencil.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func changeMode(with event: NSEvent)
```

```objc
- (void) changeModeWithEvent:(NSEvent *) event;
```

## Discussion

The default implementation passes the event to the next responder.

## Parameters

- `event`: An object encapsulating information about the change-mode event.

## See Also

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
- [func quickLook(with: NSEvent)](./quicklook%28with%29.md)
  Performs a Quick Look on the content at the location specified by the supplied event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/changemode(with:))*
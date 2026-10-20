# shouldDelayWindowOrdering(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.

**Availability**:
- macOS

## Declaration

```swift
func shouldDelayWindowOrdering(for event: NSEvent) -> Bool
```

```objc
- (BOOL) shouldDelayWindowOrderingForEvent:(NSEvent *) event;
```

#### Return Value

If this method returns [`true`](../../Swift/true.md), the normal window-ordering and activation mechanism is delayed (not necessarily prevented) until the next mouse-up event. If it returns [`false`](../../Swift/false.md), then normal ordering and activation occur.

#### Discussion

Never invoke this method directly; it’s invoked automatically for each mouse-down event directed at the NSView.

An `NSView` subclass that allows dragging should implement this method to return [`true`](../../Swift/true.md) if `theEvent` is potentially the beginning of a dragging session or of some other context where window ordering isn’t appropriate. This method is invoked before a [`mouseDown(with:)`](../nsresponder/mousedown%28with%29.md) message for `theEvent` is sent. The default implementation returns [`false`](../../Swift/false.md).

If, after delaying window ordering, the view actually initiates a dragging session or similar operation, it should also send a [`preventWindowOrdering()`](../nsapplication/preventwindowordering%28%29.md) message to `NSApp`, which completely prevents the window from ordering forward and the activation from becoming active. [`preventWindowOrdering()`](../nsapplication/preventwindowordering%28%29.md) is sent automatically by the `dragImage:` and `dragFile:` methods of `NSView`.

## Parameters

- `event`: An object representing an initial mouse-down event.

## See Also

### Dragging Operations
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](./registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
- [func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?](./begindraggingsession%28items,gesture,source%29.md)
  Initiates a drag operation using a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/shoulddelaywindowordering(for:))*
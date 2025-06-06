# shouldDelayWindowOrdering(for:)

**Framework**: AppKit  
**Kind**: method

Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldDelayWindowOrdering(for event: NSEvent) -> Bool
```

#### Return Value

If this method returns [`true`](https://developer.apple.com/documentation/swift/true), the normal window-ordering and activation mechanism is delayed (not necessarily prevented) until the next mouse-up event. If it returns [`false`](https://developer.apple.com/documentation/swift/false), then normal ordering and activation occur.

#### Discussion

Never invoke this method directly; it’s invoked automatically for each mouse-down event directed at the NSView.

An `NSView` subclass that allows dragging should implement this method to return [`true`](https://developer.apple.com/documentation/swift/true) if `theEvent` is potentially the beginning of a dragging session or of some other context where window ordering isn’t appropriate. This method is invoked before a [`mouseDown(with:)`](nsresponder/mousedown(with:).md) message for `theEvent` is sent. The default implementation returns [`false`](https://developer.apple.com/documentation/swift/false).

If, after delaying window ordering, the view actually initiates a dragging session or similar operation, it should also send a [`preventWindowOrdering()`](nsapplication/preventwindowordering().md) message to `NSApp`, which completely prevents the window from ordering forward and the activation from becoming active. [`preventWindowOrdering()`](nsapplication/preventwindowordering().md) is sent automatically by the `dragImage:` and `dragFile:` methods of `NSView`.

## Parameters

- `event`: An object representing an initial mouse-down event.

## See Also

- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](nsview/registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/shoulddelaywindowordering(for:))*
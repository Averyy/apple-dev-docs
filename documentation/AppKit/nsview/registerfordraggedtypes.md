# registerForDraggedTypes(_:)

**Framework**: AppKit  
**Kind**: method

Registers the pasteboard types that the view will accept as the destination of an image-dragging session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func registerForDraggedTypes(_ newTypes: [NSPasteboard.PasteboardType])
```

#### Discussion

Registering an `NSView` object for dragged types automatically makes it a candidate destination object for a dragging session. As such, it must properly implement some or all of the `NSDraggingDestination` protocol methods. As a convenience, `NSView` provides default implementations of these methods. See the [`NSDraggingDestination`](nsdraggingdestination.md) protocol specification for details.

## Parameters

- `newTypes`: An array of  . See   for descriptions of the pasteboard type identifiers.

## See Also

- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](nsview/registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/registerfordraggedtypes(_:))*
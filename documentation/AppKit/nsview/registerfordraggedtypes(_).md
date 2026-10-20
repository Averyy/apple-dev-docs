# registerForDraggedTypes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers the pasteboard types that the view will accept as the destination of an image-dragging session.

**Availability**:
- macOS

## Declaration

```swift
func registerForDraggedTypes(_ newTypes: [NSPasteboard.PasteboardType])
```

```objc
- (void) registerForDraggedTypes:(NSArray<NSString *> *) newTypes;
```

#### Discussion

Registering an `NSView` object for dragged types automatically makes it a candidate destination object for a dragging session. As such, it must properly implement some or all of the `NSDraggingDestination` protocol methods. As a convenience, `NSView` provides default implementations of these methods. See the [`NSDraggingDestination`](../nsdraggingdestination.md) protocol specification for details.

## Parameters

- `newTypes`: An array of [Uniform Type Identifier](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60). See [System-Declared Uniform Type Identifiers](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html#//apple_ref/doc/uid/TP40009259) for descriptions of the pasteboard type identifiers.

## See Also

### Dragging Operations
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](./registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
- [func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?](./begindraggingsession%28items,gesture,source%29.md)
  Initiates a drag operation using a gesture recognizer.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/registerfordraggedtypes(_:))*
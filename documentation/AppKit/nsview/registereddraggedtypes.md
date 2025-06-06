# registeredDraggedTypes

**Framework**: AppKit  
**Kind**: property

The array of pasteboard drag types that the view can accept.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var registeredDraggedTypes: [NSPasteboard.PasteboardType] { get }
```

#### Discussion

This property contains an array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which corresponds to a [`Uniform Type Identifier`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60). The array elements are in no particular order, but the array is guaranteed not to contain duplicate entries. To register your view’s drag types, use the [`registerForDraggedTypes(_:)`](nsview/registerfordraggedtypes(_:).md) method.

## See Also

- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/registereddraggedtypes)*
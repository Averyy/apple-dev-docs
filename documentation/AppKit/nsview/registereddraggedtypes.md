# registeredDraggedTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of pasteboard drag types that the view can accept.

**Availability**:
- macOS

## Declaration

```swift
var registeredDraggedTypes: [NSPasteboard.PasteboardType] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * registeredDraggedTypes;
```

#### Discussion

This property contains an array of [`NSString`](../../Foundation/nsstring.md) objects, each of which corresponds to a [Uniform Type Identifier](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60). The array elements are in no particular order, but the array is guaranteed not to contain duplicate entries. To register your view’s drag types, use the [`registerForDraggedTypes(_:)`](./registerfordraggedtypes%28_%29.md) method.

## See Also

### Dragging Operations
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the view as a possible destination in a dragging session.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
- [func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?](./begindraggingsession%28items,gesture,source%29.md)
  Initiates a drag operation using a gesture recognizer.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/registereddraggedtypes)*
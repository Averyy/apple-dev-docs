# beginDraggingSession(items:event:source:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 15.0+

## Declaration

```swift
func beginDraggingSession(items: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession
```

```objc
- (NSDraggingSession *) beginDraggingSessionWithItems:(NSArray<NSDraggingItem *> *) items event:(NSEvent *) event source:(id<NSDraggingSource>) source;
```

## See Also

### Dragging Items
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers a set of pasteboard types that the window accepts as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the window as a possible destination for dragging operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/begindraggingsession(items:event:source:))*
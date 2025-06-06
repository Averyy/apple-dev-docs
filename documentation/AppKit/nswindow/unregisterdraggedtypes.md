# unregisterDraggedTypes()

**Framework**: AppKit  
**Kind**: method

Unregisters the window as a possible destination for dragging operations.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func unregisterDraggedTypes()
```

## See Also

- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](nswindow/drag(_:at:offset:event:pasteboard:source:slideback:).md)
  Begins a dragging session.
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nswindow/registerfordraggedtypes(_:).md)
  Registers a set of pasteboard types that the window accepts as the destination of an image-dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/unregisterdraggedtypes())*
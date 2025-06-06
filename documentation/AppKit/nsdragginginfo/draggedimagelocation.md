# draggedImageLocation

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The current location of the dragged image’s origin, in the base coordinate system of the destination object’s window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var draggedImageLocation: NSPoint { get }
```

#### Discussion

The image moves along with the mouse pointer (the position of which is given by [`draggingLocation`](nsdragginginfo/dragginglocation.md)) but may be positioned at some offset.

## See Also

- [var draggedImage: NSImage?](nsdragginginfo/draggedimage.md)
  The image that represents the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggedimagelocation)*
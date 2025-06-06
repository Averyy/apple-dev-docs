# draggedImage

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The image that represents the dragging item.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var draggedImage: NSImage? { get }
```

#### Discussion

This image object visually represents the data put on the pasteboard during the drag operation; however, it is the pasteboard data and not this image that is ultimately utilized in the dragging operation.

This method returns non-`nil` for a local drag, but `nil` for a cross-process drag. With the new multi-image dragging capabilities, a cross-process destination may participate and change the drag image. But it still cannot get the current drag image.

## See Also

- [var draggedImageLocation: NSPoint](nsdragginginfo/draggedimagelocation.md)
  The current location of the dragged image’s origin, in the base coordinate system of the destination object’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggedimage)*
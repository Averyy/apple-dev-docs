# draggedImageLocation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The current location of the dragged image’s origin, in the base coordinate system of the destination object’s window.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
var draggedImageLocation: NSPoint { get }
```

```objc
@property (readonly) NSPoint draggedImageLocation;
```

## Discussion

The image moves along with the mouse pointer (the position of which is given by [`draggingLocation`](./dragginglocation.md)) but may be positioned at some offset.

## See Also

### Getting image information
- [var draggedImage: NSImage?](./draggedimage.md)
  The image that represents the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggedimagelocation)*
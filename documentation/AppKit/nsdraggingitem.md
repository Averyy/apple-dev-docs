# NSDraggingItem

**Framework**: AppKit  
**Kind**: class

A single dragged item within a dragging session.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSDraggingItem
```

#### Overview

[`NSDraggingItem`](nsdraggingitem.md) objects have extremely limited lifetimes. Don’t retain these items because changing outside of the prescribed lifetimes has no impact on the drag.

When you call the [`NSDraggingSession`](nsdraggingsession.md) method [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md), the system immediately consumes the dragging items that pass to the method, and doesn’t retain them. Any further changes to the dragging item associated with the returned [`NSDraggingSession`](nsdraggingsession.md) must occur with the enumeration method [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdraggingsession/enumeratedraggingitems(options:for:classes:searchoptions:using:).md). When enumerating, the system creates `NSDraggingItem` instances right before giving them to the enumeration block. After returning from the block, the dragging item is no longer valid.

## Topics

### Initializing a dragging item
- [init(pasteboardWriter: any NSPasteboardWriting)](nsdraggingitem/init(pasteboardwriter:).md)
  Creates and returns a dragging item using the specified content.
### Dragging frame
- [func setDraggingFrame(NSRect, contents: Any?)](nsdraggingitem/setdraggingframe(_:contents:).md)
  Sets the item’s dragging frame and contents.
- [var draggingFrame: NSRect](nsdraggingitem/draggingframe.md)
  The frame of the dragging item.
### Drag image components
- [var imageComponents: [NSDraggingImageComponent]?](nsdraggingitem/imagecomponents.md)
  An array of dragging image components to use to create the drag image.
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](nsdraggingitem/imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [NSDraggingItem.ImageComponentKey](nsdraggingitem/imagecomponentkey.md)
  Keys that identify components of a dragging image.
- [var item: Any](nsdraggingitem/item.md)
  The pasteboard reader or writer object dependent on the context where you use the dragging item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSDraggingSource](nsdraggingsource.md)
  A set of methods that are implemented by the source object in a dragging session.
- [class NSDraggingSession](nsdraggingsession.md)
  The encapsulation of a drag-and-drop action that supports modification of the drag while in progress.
- [class NSDraggingImageComponent](nsdraggingimagecomponent.md)
  A single object in a dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem)*
# NSDraggingSource

**Framework**: AppKit  
**Kind**: protocol

A set of methods that are implemented by the source object in a dragging session.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSDraggingSource : NSObjectProtocol
```

#### Overview

In macOS 10.7 and later `NSDraggingSource` is now a formal protocol and has an updated interface. The OS X v10.6 behavior has been retained, but will be dropped in a future version of the operating system. The methods that are to be deprecated are marked as such.

## Topics

### Dragging Session Operation
- [func draggingSession(NSDraggingSession, sourceOperationMaskFor: NSDraggingContext) -> NSDragOperation](nsdraggingsource/draggingsession(_:sourceoperationmaskfor:).md)
  Declares the types of operations the source allows to be performed.
### Dragging Session Locations
- [func draggingSession(NSDraggingSession, willBeginAt: NSPoint)](nsdraggingsource/draggingsession(_:willbeginat:).md)
  Invoked when the drag will begin.
- [func draggingSession(NSDraggingSession, movedTo: NSPoint)](nsdraggingsource/draggingsession(_:movedto:).md)
  Invoked when the drag moves on the screen.
- [func draggingSession(NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nsdraggingsource/draggingsession(_:endedat:operation:).md)
  Invoked when the dragging session has completed.
### Dragging Session Modifier Keys
- [func ignoreModifierKeys(for: NSDraggingSession) -> Bool](nsdraggingsource/ignoremodifierkeys(for:).md)
  Returns whether the modifier keys will be ignored for this dragging session.
### Dragging Options
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](../ObjectiveC/NSObject-swift.class/namesOfPromisedFilesDropped(atDestination:).md)
  Returns the names of the files that the receiver promises to create at a specified location.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSCollectionView](nscollectionview.md)
- [NSOutlineView](nsoutlineview.md)
- [NSTableView](nstableview.md)
- [NSTextView](nstextview.md)

## See Also

- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [class NSDraggingItem](nsdraggingitem.md)
  A single dragged item within a dragging session.
- [class NSDraggingSession](nsdraggingsession.md)
  The encapsulation of a drag-and-drop action that supports modification of the drag while in progress.
- [class NSDraggingImageComponent](nsdraggingimagecomponent.md)
  A single object in a dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource)*
# NSDraggingSource

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that are implemented by the source object in a dragging session.

**Availability**:
- macOS

## Declaration

```swift
protocol NSDraggingSource : NSObjectProtocol
```

```objc
@protocol NSDraggingSource <NSObject>
```

#### Overview

In macOS 10.7 and later `NSDraggingSource` is now a formal protocol and has an updated interface. The OS X v10.6 behavior has been retained, but will be dropped in a future version of the operating system. The methods that are to be deprecated are marked as such.

## Topics

### Dragging Session Operation
- [func draggingSession(NSDraggingSession, sourceOperationMaskFor: NSDraggingContext) -> NSDragOperation](./nsdraggingsource/draggingsession%28_,sourceoperationmaskfor%29.md)
  Declares the types of operations the source allows to be performed.
### Dragging Session Locations
- [func draggingSession(NSDraggingSession, willBeginAt: NSPoint)](./nsdraggingsource/draggingsession%28_,willbeginat%29.md)
  Invoked when the drag will begin.
- [func draggingSession(NSDraggingSession, movedTo: NSPoint)](./nsdraggingsource/draggingsession%28_,movedto%29.md)
  Invoked when the drag moves on the screen.
- [func draggingSession(NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./nsdraggingsource/draggingsession%28_,endedat,operation%29.md)
  Invoked when the dragging session has completed.
### Dragging Session Modifier Keys
- [func ignoreModifierKeys(for: NSDraggingSession) -> Bool](./nsdraggingsource/ignoremodifierkeys%28for%29.md)
  Returns whether the modifier keys will be ignored for this dragging session.
### Dragging Options
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](../ObjectiveC/nsobject-swift.class/namesofpromisedfilesdropped%28atdestination%29.md)
  Returns the names of the files that the receiver promises to create at a specified location.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSCollectionView](./nscollectionview.md)
- [NSOutlineView](./nsoutlineview.md)
- [NSTableView](./nstableview.md)
- [NSTextView](./nstextview.md)

## See Also

### Related Documentation
- [Drag and Drop](./drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
### Drag Sources
- [class NSDraggingItem](./nsdraggingitem.md)
  A single dragged item within a dragging session.
- [class NSDraggingSession](./nsdraggingsession.md)
  An object that encapsulates a drag-and-drop action.
- [class NSDraggingImageComponent](./nsdraggingimagecomponent.md)
  A single object in a dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource)*
# NSDraggingSession

**Framework**: AppKit  
**Kind**: class

An object that encapsulates a drag-and-drop action.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSDraggingSession
```

#### Overview

You start a new dragging session by calling [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md) or [`beginDraggingSession(items:gesture:source:)`](nsview/begindraggingsession(items:gesture:source:).md) on an `NSView`. The method immediately returns, and the actual drag begins at the next turn of the run loop.

## Topics

### Dragging Pasteboard
- [var draggingPasteboard: NSPasteboard](nsdraggingsession/draggingpasteboard.md)
  Returns the pasteboard object that contains the data being dragged.
### Dragging Visual Representation
- [var animatesToStartingPositionsOnCancelOrFail: Bool](nsdraggingsession/animatestostartingpositionsoncancelorfail.md)
  Controls whether the dragging image animates back to its starting point on a cancelled or failed drag.
- [var draggingFormation: NSDraggingFormation](nsdraggingsession/draggingformation.md)
  Controls the dragging formation when the drag is not over the source or a valid destination.
### Identifying the Dragging Session
- [var draggingSequenceNumber: Int](nsdraggingsession/draggingsequencenumber.md)
  Returns a number that uniquely identifies the dragging session.
### Enumerating Dragging Items
- [func enumerateDraggingItems(options: NSDraggingItemEnumerationOptions, for: NSView?, classes: [AnyClass], searchOptions: [NSPasteboard.ReadingOptionKey : Any], using: (NSDraggingItem, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdraggingsession/enumeratedraggingitems(options:for:classes:searchoptions:using:).md)
  Enumerates through each dragging item.
### Dragging Session Location
- [var draggingLocation: NSPoint](nsdraggingsession/dragginglocation.md)
  The current cursor location of the drag in screen coordinates.
### Dragging Item Location
- [var draggingLeaderIndex: Int](nsdraggingsession/draggingleaderindex.md)
  The index of the dragging item under the cursor.
### Instance Methods
- [func updateDrag(from: NSGestureRecognizer)](nsdraggingsession/updatedrag(from:).md)

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
- [class NSDraggingItem](nsdraggingitem.md)
  A single dragged item within a dragging session.
- [class NSDraggingImageComponent](nsdraggingimagecomponent.md)
  A single object in a dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsession)*
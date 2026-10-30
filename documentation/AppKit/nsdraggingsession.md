# NSDraggingSession

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that encapsulates a drag-and-drop action.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSDraggingSession
```

```objc
@interface NSDraggingSession : NSObject
```

## Overview

You start a new dragging session by calling [`beginDraggingSession(with:event:source:)`](./nsview/begindraggingsession%28with,event,source%29.md) or [`beginDraggingSession(items:gesture:source:)`](./nsview/begindraggingsession%28items,gesture,source%29.md) on an `NSView`. The method immediately returns, and the actual drag begins at the next turn of the run loop.

### Dragging sessions from gesture recognizers

[`NSDraggingSession`](./nsdraggingsession.md) provides APIs for better interoperation with gesture recognizers. Use [`beginDraggingSession(items:gesture:source:)`](./nsview/begindraggingsession%28items,gesture,source%29.md) to start a drag from a gesture recognizer. This replaces the tracking-loop-based [`beginDraggingSession(with:event:source:)`](./nsview/begindraggingsession%28with,event,source%29.md). AppKit cancels the initiating gesture recognizer during the drag, but the timing differs by input type: for a mouse-based gesture, cancellation happens at the end of the operation; for a touch-based gesture, it happens at the very start.

## Topics

### Dragging Pasteboard
- [var draggingPasteboard: NSPasteboard](./nsdraggingsession/draggingpasteboard.md)
  Returns the pasteboard object that contains the data being dragged.
### Dragging Visual Representation
- [var animatesToStartingPositionsOnCancelOrFail: Bool](./nsdraggingsession/animatestostartingpositionsoncancelorfail.md)
  Controls whether the dragging image animates back to its starting point on a cancelled or failed drag.
- [var draggingFormation: NSDraggingFormation](./nsdraggingsession/draggingformation.md)
  Controls the dragging formation when the drag is not over the source or a valid destination.
### Identifying the Dragging Session
- [var draggingSequenceNumber: Int](./nsdraggingsession/draggingsequencenumber.md)
  Returns a number that uniquely identifies the dragging session.
### Enumerating Dragging Items
- [func enumerateDraggingItems(options: NSDraggingItemEnumerationOptions, for: NSView?, classes: [AnyClass], searchOptions: [NSPasteboard.ReadingOptionKey : Any], using: (NSDraggingItem, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsdraggingsession/enumeratedraggingitems%28options,for,classes,searchoptions,using%29.md)
  Enumerates through each dragging item.
### Dragging Session Location
- [var draggingLocation: NSPoint](./nsdraggingsession/dragginglocation.md)
  The current cursor location of the drag in screen coordinates.
### Dragging Item Location
- [var draggingLeaderIndex: Int](./nsdraggingsession/draggingleaderindex.md)
  The index of the dragging item under the cursor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Drag Sources
- [protocol NSDraggingSource](./nsdraggingsource.md)
  A set of methods that are implemented by the source object in a dragging session.
- [class NSDraggingItem](./nsdraggingitem.md)
  A single dragged item within a dragging session.
- [class NSDraggingImageComponent](./nsdraggingimagecomponent.md)
  A single object in a dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsession)*
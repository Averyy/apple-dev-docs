# draggingSourceOperationMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Information about the dragging operation and the data it contains.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
var draggingSourceOperationMask: NSDragOperation { get }
```

```objc
@property (readonly) NSDragOperation draggingSourceOperationMask;
```

## Discussion

The dragging source ([`NSDraggingSource`](../nsdraggingsource.md)) declares the dragging operation mask through [`draggingSession(_:sourceOperationMaskFor:)`](../nsdraggingsource/draggingsession%28_,sourceoperationmaskfor%29.md).

If the source doesn’t permit dragging operations, the value of the dragging source operation mask is [`NSDragOperationNone`](../nsdragoperation/nsdragoperationnone.md), or the empty option set in Swift (`[]`). If the source permits dragging operations, the value of the dragging source operation mask is the result of a bitwise OR operation on one or more of the [`NSDragOperation`](../nsdragoperation.md) constants in Objective-C, or an option set containing one or more of the [`NSDragOperation`](../nsdragoperation.md) constants in Swift.

If the user holds down a modifier key during the dragging session and the dragging source allows modifier keys to affect the drag operation, the system combines the dragging source operation mask with the value that corresponds to the modifier key. You control whether the modifier keys can affect the drag operation using the dragging source’s [`ignoreModifierKeys(for:)`](../nsdraggingsource/ignoremodifierkeys%28for%29.md) method.

| Modifier Key | Dragging Operation |
| --- | --- |
| Option | [`copy`](../nsdragoperation/copy.md) |
| Command | [`move`](../nsdragoperation/move.md) |
| Option and Command | [`link`](../nsdragoperation/link.md) |

## See Also

### Obtaining information about the dragging session
- [var draggingPasteboard: NSPasteboard](./draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](./draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](./draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingLocation: NSPoint](./dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](./draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](./numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](./namesofpromisedfilesdropped%28atdestination%29.md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggingsourceoperationmask)*
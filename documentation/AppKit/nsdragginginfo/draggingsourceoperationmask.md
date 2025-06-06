# draggingSourceOperationMask

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

Information about the dragging operation and the data it contains.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var draggingSourceOperationMask: NSDragOperation { get }
```

#### Discussion

The dragging source ([`NSDraggingSource`](nsdraggingsource.md)) declares the dragging operation mask through [`draggingSession(_:sourceOperationMaskFor:)`](nsdraggingsource/draggingsession(_:sourceoperationmaskfor:).md).

If the source doesn’t permit dragging operations, the value of the dragging source operation mask is [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md), or the empty option set in Swift (`[]`). If the source permits dragging operations, the value of the dragging source operation mask is the result of a bitwise OR operation on one or more of the [`NSDragOperation`](nsdragoperation.md) constants in Objective-C, or an option set containing one or more of the [`NSDragOperation`](nsdragoperation.md) constants in Swift.

If the user holds down a modifier key during the dragging session and the dragging source allows modifier keys to affect the drag operation, the system combines the dragging source operation mask with the value that corresponds to the modifier key. You control whether the modifier keys can affect the drag operation using the dragging source’s [`ignoreModifierKeys(for:)`](nsdraggingsource/ignoremodifierkeys(for:).md) method.

| Modifier Key | Dragging Operation |
| --- | --- |
| Option | [`copy`](nsdragoperation/copy.md) |
| Command | [`move`](nsdragoperation/move.md) |
| Option and Command | [`link`](nsdragoperation/link.md) |

## See Also

- [var draggingPasteboard: NSPasteboard](nsdragginginfo/draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](nsdragginginfo/draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](nsdragginginfo/draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingLocation: NSPoint](nsdragginginfo/dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](nsdragginginfo/draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](nsdragginginfo/numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](nsdragginginfo/namesofpromisedfilesdropped(atdestination:).md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggingsourceoperationmask)*
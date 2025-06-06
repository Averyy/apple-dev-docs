# draggingDestinationWindow

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The destination window for the dragging operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var draggingDestinationWindow: NSWindow? { get }
```

#### Discussion

Either this window is the destination itself, or it contains the view object that is the destination.

## See Also

- [var draggingPasteboard: NSPasteboard](nsdragginginfo/draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](nsdragginginfo/draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](nsdragginginfo/draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingSourceOperationMask: NSDragOperation](nsdragginginfo/draggingsourceoperationmask.md)
  Information about the dragging operation and the data it contains.
- [var draggingLocation: NSPoint](nsdragginginfo/dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var numberOfValidItemsForDrop: Int](nsdragginginfo/numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](nsdragginginfo/namesofpromisedfilesdropped(atdestination:).md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggingdestinationwindow)*
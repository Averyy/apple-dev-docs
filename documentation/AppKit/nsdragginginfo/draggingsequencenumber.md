# draggingSequenceNumber

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

A number that uniquely identifies the dragging session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var draggingSequenceNumber: Int { get }
```

## See Also

- [var draggingPasteboard: NSPasteboard](nsdragginginfo/draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSource: Any?](nsdragginginfo/draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingSourceOperationMask: NSDragOperation](nsdragginginfo/draggingsourceoperationmask.md)
  Information about the dragging operation and the data it contains.
- [var draggingLocation: NSPoint](nsdragginginfo/dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](nsdragginginfo/draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](nsdragginginfo/numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](nsdragginginfo/namesofpromisedfilesdropped(atdestination:).md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/draggingsequencenumber)*
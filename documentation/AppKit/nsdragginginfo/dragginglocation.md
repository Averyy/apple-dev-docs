# draggingLocation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The current location of the mouse pointer in the base coordinate system of the destination object’s window.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
var draggingLocation: NSPoint { get }
```

```objc
@property (readonly) NSPoint draggingLocation;
```

## See Also

### Obtaining information about the dragging session
- [var draggingPasteboard: NSPasteboard](./draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](./draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](./draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingSourceOperationMask: NSDragOperation](./draggingsourceoperationmask.md)
  Information about the dragging operation and the data it contains.
- [var draggingDestinationWindow: NSWindow?](./draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](./numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](./namesofpromisedfilesdropped%28atdestination%29.md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/dragginglocation)*
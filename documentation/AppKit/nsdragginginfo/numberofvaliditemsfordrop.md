# numberOfValidItemsForDrop

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of valid items for a drop operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var numberOfValidItemsForDrop: Int { get set }
```

```objc
@property NSInteger numberOfValidItemsForDrop;
```

## Discussion

During draggingEntered: or draggingUpdated:, you are responsible for returning the drag operation. In some cases, you may accept some, but not all items on the dragging pasteboard. (For example, your application may only accept image files.)

If you only accept some of the items, set this property to the number of items accepted so the drag manager can update the drag count badge.

When [`updateDraggingItemsForDrag(_:)`](../nsdraggingdestination/updatedraggingitemsfordrag%28_%29.md) is called, you should set the image of non-valid dragging items to `nil`. If none of the drag items are valid then you should not `updateItems:`, simply return [`NSDragOperationNone`](../nsdragoperation/nsdragoperationnone.md) from your implementation of draggingEntered: and, or draggingUpdated: and do not modify any drag item properties.

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
- [var draggingLocation: NSPoint](./dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](./draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](./namesofpromisedfilesdropped%28atdestination%29.md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/numberofvaliditemsfordrop)*
# collectionView(_:acceptDrop:indexPath:dropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Incorporates the dropped content into the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, acceptDrop draggingInfo: any NSDraggingInfo, indexPath: IndexPath, dropOperation: NSCollectionView.DropOperation) -> Bool
```

```objc
- (BOOL) collectionView:(NSCollectionView *) collectionView acceptDrop:(id<NSDraggingInfo>) draggingInfo indexPath:(NSIndexPath *) indexPath dropOperation:(NSCollectionViewDropOperation) dropOperation;
```

#### Return Value

[`true`](../../Swift/true.md) if the drop operation should be accepted or [`false`](../../Swift/false.md) if it should be rejected.

#### Discussion

The collection view calls this method when the user releases the mouse button while it is over a valid drop target. This method is called after the [`collectionView(_:validateDrop:proposedIndexPath:dropOperation:)`](./collectionview%28_,validatedrop,proposedindexpath,dropoperation%29.md) method validates that dropping the content at the specified location is possible. You must implement this method to accept the dropped content and incorporate it into the collection view.

In your implementation, use the information in the `draggingInfo` parameter to retrieve the data, update your data source object, and insert the appropriate items into the collection view. The dropped data is stored in the [`draggingPasteboard`](../nsdragginginfo/draggingpasteboard.md) property of the dragging information object.

If the [`animatesToDestination`](../nsdragginginfo/animatestodestination.md) property of the dragging information is [`true`](../../Swift/true.md), update the image and frame for each dragged item to its new location in the collection view.  You can enumerate the list of dragged items using the [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](../nsdragginginfo/enumeratedraggingitems%28options,for,classes,searchoptions,using%29.md) method of the dragging information object.

## Parameters

- `collectionView`: The collection view receiving the dropped content.
- `draggingInfo`: The information about the drag operation.
- `indexPath`: The index path at which the drop occurred. Use this location as the insertion point for the content.
- `dropOperation`: The type of drop operation to perform.

## See Also

### Drag and Drop Support
- [Supporting Collection View Drag and Drop Through File Promises](../supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func collectionView(NSCollectionView, canDragItemsAt: Set<IndexPath>, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-49wix.md)
  Returns a Boolean indicating whether a drag operation involving the specified items can begin.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: IndexPath) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md)
  Provides the pasteboard writer for the item at the specified index path.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: Set<IndexPath>, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-898js.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: Set<IndexPath>)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-68x2y.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, endedAt: NSPoint, dragOperation: NSDragOperation)](./collectionview%28_,draggingsession,endedat,dragoperation%29.md)
  Notifies your delegate that a drag session ended.
- [func collectionView(NSCollectionView, updateDraggingItemsForDrag: any NSDraggingInfo)](./collectionview%28_,updatedraggingitemsfordrag%29.md)
  Asks your delegate to update the dragging items during a drag operation.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndexPath: AutoreleasingUnsafeMutablePointer<NSIndexPath>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](./collectionview%28_,validatedrop,proposedindexpath,dropoperation%29.md)
  Validates whether a drop operation is possible at the specified location.
- [func collectionView(NSCollectionView, writeItemsAt: Set<IndexPath>, to: NSPasteboard) -> Bool](./collectionview%28_,writeitemsat,to%29-23ozm.md)
  Places the data for the drag operation on the pasteboard.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: Set<IndexPath>) -> [String]](./collectionview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditemsat%29-6yag4.md)
  Returns the names of the promised files that you created for a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:acceptdrop:indexpath:dropoperation:))*
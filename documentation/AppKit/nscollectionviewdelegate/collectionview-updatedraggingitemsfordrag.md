# collectionView(_:updateDraggingItemsForDrag:)

**Framework**: AppKit  
**Kind**: method

Asks your delegate to update the dragging items during a drag operation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, updateDraggingItemsForDrag draggingInfo: any NSDraggingInfo)
```

#### Discussion

You can use this method to update the current drag items while a drag is in progress. Updating the drag items is optional, but you might use this method to change the image for an item. For example, you might change the image when the mouse hovers over a particular part of the collection view. Use the [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdragginginfo/enumeratedraggingitems(options:for:classes:searchoptions:using:).md) method of the `draggingInfo` parameter to iterate over the drag items and update them as appropriate.

## Parameters

- `collectionView`: The collection view asking you to update the dragging items.
- `draggingInfo`: The current information for the drag operation. Use this object to iterate over the dragging items.

## See Also

- [Supporting Collection View Drag and Drop Through File Promises](supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func collectionView(NSCollectionView, canDragItemsAt: Set<IndexPath>, with: NSEvent) -> Bool](nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-49wix.md)
  Returns a Boolean indicating whether a drag operation involving the specified items can begin.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: IndexPath) -> (any NSPasteboardWriting)?](nscollectionviewdelegate/collectionview(_:pasteboardwriterforitemat:)-5eyyl.md)
  Provides the pasteboard writer for the item at the specified index path.
- [func collectionView(NSCollectionView, writeItemsAt: Set<IndexPath>, to: NSPasteboard) -> Bool](nscollectionviewdelegate/collectionview(_:writeitemsat:to:)-23ozm.md)
  Places the data for the drag operation on the pasteboard.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: Set<IndexPath>) -> [String]](nscollectionviewdelegate/collectionview(_:namesofpromisedfilesdroppedatdestination:fordraggeditemsat:)-6yag4.md)
  Returns the names of the promised files that you created for a drag operation.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: Set<IndexPath>, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-898js.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: Set<IndexPath>)](nscollectionviewdelegate/collectionview(_:draggingsession:willbeginat:foritemsat:)-68x2y.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, endedAt: NSPoint, dragOperation: NSDragOperation)](nscollectionviewdelegate/collectionview(_:draggingsession:endedat:dragoperation:).md)
  Notifies your delegate that a drag session ended.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndexPath: AutoreleasingUnsafeMutablePointer<NSIndexPath>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindexpath:dropoperation:).md)
  Validates whether a drop operation is possible at the specified location.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, indexPath: IndexPath, dropOperation: NSCollectionView.DropOperation) -> Bool](nscollectionviewdelegate/collectionview(_:acceptdrop:indexpath:dropoperation:).md)
  Incorporates the dropped content into the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:updatedraggingitemsfordrag:))*
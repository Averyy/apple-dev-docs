# collectionView(_:validateDrop:proposedIndexPath:dropOperation:)

**Framework**: AppKit  
**Kind**: method

Validates whether a drop operation is possible at the specified location.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, validateDrop draggingInfo: any NSDraggingInfo, proposedIndexPath proposedDropIndexPath: AutoreleasingUnsafeMutablePointer<NSIndexPath>, dropOperation proposedDropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation
```

#### Return Value

A value that indicates which dragging operation to perform. Return [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md) to disallow a drop at the proposed location.

#### Discussion

Although implementation of this method is optional, you must implement it to support drops onto the associated collection view. You must also call the collection view’s [`registerForDraggedTypes(_:)`](nsview/registerfordraggedtypes(_:).md) method to register the types of drops it supports. If you do not perform both of these actions, the collection view does not accept drops.

When an interactive drag operation occurs, the collection view calls this method to determine whether the current mouse location is a valid place to drop the content. This method may be called many times during the course of the drag operation. Your implementation should look at the proposed location and return a constant that reflects how the drop would be handled.

While validating the drop location, you can suggest a better drop location by updating the values in the `proposedDropIndexPath` and `proposedDropOperation` parameters. For example, you might suggest dropping the content before the specified item instead of on it. The collection view sets the `proposedDropOperation` parameter to [`NSCollectionView.DropOperation.on`](nscollectionview/dropoperation/on.md) when the mouse is closer to the middle of an item than to its edges; otherwise, it sets the parameter to [`NSCollectionView.DropOperation.before`](nscollectionview/dropoperation/before.md).

## Parameters

- `collectionView`: The collection view asking you to validate the drop operation.
- `draggingInfo`: The information about the drag operation.
- `proposedDropIndexPath`: The index path at which the drop would occur. This parameter is passed by-reference and can be modified to change the proposed index path.
- `proposedDropOperation`: The type of drop operation being proposed. This parameter is passed by-reference and can be modified to change the drop operation type.

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
- [func collectionView(NSCollectionView, updateDraggingItemsForDrag: any NSDraggingInfo)](nscollectionviewdelegate/collectionview(_:updatedraggingitemsfordrag:).md)
  Asks your delegate to update the dragging items during a drag operation.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, indexPath: IndexPath, dropOperation: NSCollectionView.DropOperation) -> Bool](nscollectionviewdelegate/collectionview(_:acceptdrop:indexpath:dropoperation:).md)
  Incorporates the dropped content into the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:validatedrop:proposedindexpath:dropoperation:))*
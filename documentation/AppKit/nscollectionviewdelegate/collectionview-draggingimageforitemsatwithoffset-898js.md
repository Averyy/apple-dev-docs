# collectionView(_:draggingImageForItemsAt:with:offset:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a drag image to represent the specified items during a drag.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, draggingImageForItemsAt indexPaths: Set<IndexPath>, with event: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

#### Return Value

The image to use for the dragged items.

#### Discussion

Your implementation of this method should create an appropriate image to use during the drag operation.  The collection view places the center of your image at the current mouse location. Update the value in the `dragImageOffset` parameter to shift the position of your image by the specified amount.

If you do not implement this method, the collection view uses the drag image returned by the [`draggingImageForItems(at:with:offset:)`](nscollectionview/draggingimageforitems(at:with:offset:)-7rc4k.md) method instead.

## Parameters

- `collectionView`: The collection view making the request.
- `indexPaths`: The index paths of the items being dragged.
- `event`: The mouse-down event that began the drag operation. You can use the mouse location when determining what value to return in the   parameter.
- `dragImageOffset`: The offset value to use when positioning the image. On input, the point is  , which centers the returned image under the mouse. Your method can return a different point that repositions the drag image by the specified offset values.

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
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: Set<IndexPath>)](nscollectionviewdelegate/collectionview(_:draggingsession:willbeginat:foritemsat:)-68x2y.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, endedAt: NSPoint, dragOperation: NSDragOperation)](nscollectionviewdelegate/collectionview(_:draggingsession:endedat:dragoperation:).md)
  Notifies your delegate that a drag session ended.
- [func collectionView(NSCollectionView, updateDraggingItemsForDrag: any NSDraggingInfo)](nscollectionviewdelegate/collectionview(_:updatedraggingitemsfordrag:).md)
  Asks your delegate to update the dragging items during a drag operation.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndexPath: AutoreleasingUnsafeMutablePointer<NSIndexPath>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindexpath:dropoperation:).md)
  Validates whether a drop operation is possible at the specified location.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, indexPath: IndexPath, dropOperation: NSCollectionView.DropOperation) -> Bool](nscollectionviewdelegate/collectionview(_:acceptdrop:indexpath:dropoperation:).md)
  Incorporates the dropped content into the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-898js)*
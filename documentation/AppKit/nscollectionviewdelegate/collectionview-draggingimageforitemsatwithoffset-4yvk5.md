# collectionView(_:draggingImageForItemsAt:with:offset:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a drag image to represent the specified items during a drag.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, draggingImageForItemsAt indexes: IndexSet, with event: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

#### Return Value

The image to use for the dragged items.

#### Discussion

If the delegate does not implement this method, the collection view uses the image returned by [`draggingImageForItems(at:with:offset:)`](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md).

You do not need to implement this method for your collection view to be a drag source.

## Parameters

- `collectionView`: The collection view making the request.
- `indexes`: The indexes of the items being dragged.
- `event`: The mouse-down event that initiated the drag.
- `dragImageOffset`: An in/out parameter that is initially set to  , which causes the image to be centered under the mouse. The value can be modified to reposition the returned image.

## See Also

- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](nscollectionviewdelegate/collectionview(_:pasteboardwriterforitemat:)-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
- [func collectionView(NSCollectionView, writeItemsAt: IndexSet, to: NSPasteboard) -> Bool](nscollectionviewdelegate/collectionview(_:writeitemsat:to:)-a1lk.md)
  Invoked after it has been determined that a drag should begin, but before the drag has been started.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: IndexSet) -> [String]](nscollectionviewdelegate/collectionview(_:namesofpromisedfilesdroppedatdestination:fordraggeditemsat:)-wwec.md)
  Invoked to return an array of filenames that the receiver promises to create.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: IndexSet)](nscollectionviewdelegate/collectionview(_:draggingsession:willbeginat:foritemsat:)-cpuq.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndex: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindex:dropoperation:).md)
  Validates the specified location to see if it is a valid drop target.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:).md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-4yvk5)*
# collectionView(_:pasteboardWriterForItemAt:)

**Framework**: AppKit  
**Kind**: method

Provides the pasteboard writer for the item at the specified index

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, pasteboardWriterForItemAt index: Int) -> (any NSPasteboardWriting)?
```

#### Return Value

The pasteboard writer object to use for managing the item data. Return `nil` to prevent the collection view from dragging the item.

#### Discussion

The collection view calls this method for each item involved in the drag operation after it has determined that a drag should begin but before the drag operation has started.  Your implementation of this method should create and return the pasteboard writer—an object conforming to the [`NSPasteboardWriting`](nspasteboardwriting.md) protocol—to use for providing the item’s data. Using the object you provide, the collection view creates an [`NSDraggingItem`](nsdraggingitem.md) object for you and configures its [`draggingFrame`](nsdraggingitem/draggingframe.md) and [`imageComponents`](nsdraggingitem/imagecomponents.md) properties for you using information from the item at the specified index path.

If you implement this method, the collection view does not call the [`collectionView(_:draggingImageForItemsAt:with:offset:)`](nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-4yvk5.md) of your delegate or the [`draggingImageForItems(at:with:offset:)`](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md) method of [`NSCollectionView`](nscollectionview.md).

## Parameters

- `collectionView`: The collection view making the request.
- `index`: The index of the item requiring a pasteboard writer.

## See Also

- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, writeItemsAt: IndexSet, to: NSPasteboard) -> Bool](nscollectionviewdelegate/collectionview(_:writeitemsat:to:)-a1lk.md)
  Invoked after it has been determined that a drag should begin, but before the drag has been started.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: IndexSet) -> [String]](nscollectionviewdelegate/collectionview(_:namesofpromisedfilesdroppedatdestination:fordraggeditemsat:)-wwec.md)
  Invoked to return an array of filenames that the receiver promises to create.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-4yvk5.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: IndexSet)](nscollectionviewdelegate/collectionview(_:draggingsession:willbeginat:foritemsat:)-cpuq.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndex: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindex:dropoperation:).md)
  Validates the specified location to see if it is a valid drop target.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:).md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:pasteboardwriterforitemat:)-7ldvs)*
# collectionView(_:acceptDrop:index:dropOperation:)

**Framework**: AppKit  
**Kind**: method

Invoked when the mouse is released over a collection view that previously allowed a drop.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, acceptDrop draggingInfo: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the drop operation should be accepted, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is called when the mouse is released over a collection view that previously decided to allow a drop via the [`collectionView(_:validateDrop:proposedIndex:dropOperation:)`](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindex:dropoperation:).md) method. At this time, the delegate should incorporate the data from the dragging pasteboard and update the collection view’s contents.

You must implement this method for your collection view to be a drag destination

## Parameters

- `collectionView`: The collection view that send the message.
- `draggingInfo`: An object that contains more information about this dragging operation.
- `index`: The index of the proposed drop item.
- `dropOperation`: The type of dragging operation.

## See Also

- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](nscollectionviewdelegate/collectionview(_:pasteboardwriterforitemat:)-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:))*
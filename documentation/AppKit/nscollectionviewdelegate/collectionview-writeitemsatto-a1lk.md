# collectionView(_:writeItemsAt:to:)

**Framework**: AppKit  
**Kind**: method

Invoked after it has been determined that a drag should begin, but before the drag has been started.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func collectionView(_ collectionView: NSCollectionView, writeItemsAt indexes: IndexSet, to pasteboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to begin the drag, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

To start the drag, you must first declare the pasteboard types that are supported by sending `pasteboard` a [`declareTypes(_:owner:)`](nspasteboard/declaretypes(_:owner:).md) method. You then place the data for the items at the specified indexes on `pasteboard`, and return [`true`](https://developer.apple.com/documentation/Swift/true) from the method.

The drag image and other drag related information will be set up and provided by the view once this call returns [`true`](https://developer.apple.com/documentation/Swift/true).

You need to implement this method for your collection view to be a drag source.

## Parameters

- `collectionView`: The collection view that send the message.
- `indexes`: The indexes of the items to write to the pasteboard.
- `pasteboard`: The pasteboard containing the content from the dragged items.

## See Also

- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](nscollectionviewdelegate/collectionview(_:pasteboardwriterforitemat:)-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:writeitemsat:to:)-a1lk)*
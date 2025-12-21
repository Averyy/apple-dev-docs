# collectionView(_:canDragItemsAt:with:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean indicating whether the collection view can begin dragging the specified items.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, canDragItemsAt indexes: IndexSet, with event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the collection view can begin the drag operation for the specified items or [`false`](https://developer.apple.com/documentation/Swift/false) if it cannot.

#### Discussion

Implement this method when you want selective control over the initiation of drag operations. In your implementation, use the provided information to determine whether the drag operation should occur and return the appropriate return value. For example, you might return [`false`](https://developer.apple.com/documentation/Swift/false) if your interface does not allow the user to drag the specified items.

If you do not implement this method in your delegate object, the collection view assumes a return value of [`true`](https://developer.apple.com/documentation/Swift/true) and begins the drag operation.

## Parameters

- `collectionView`: The collection view containing the items to be dragged.
- `indexes`: The indexes of the items to be dragged.
- `event`: The mouse event that initiated the drag action.

## See Also

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
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:).md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-39rjh)*
# collectionView(_:validateDrop:proposedIndex:dropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Validates the specified location to see if it is a valid drop target.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, validateDrop draggingInfo: any NSDraggingInfo, proposedIndex proposedDropIndex: UnsafeMutablePointer<Int>, dropOperation proposedDropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation
```

```objc
- (NSDragOperation) collectionView:(NSCollectionView *) collectionView validateDrop:(id<NSDraggingInfo>) draggingInfo proposedIndex:(NSInteger *) proposedDropIndex dropOperation:(NSCollectionViewDropOperation *) proposedDropOperation;
```

## Return Value

A value that indicates which dragging operation to perform. Return [`NSDragOperationNone`](../nsdragoperation/nsdragoperationnone.md) to disallow the drop.

## Discussion

Based on the mouse position, the collection view will suggest a proposed index and drop operation. These values are in/out parameters and can be changed by the delegate to retarget the drop operation.

The collection view will propose `NSCollectionViewDropOn` when the dragging location is closer to the middle of the item than either of its edges. Otherwise, it will propose `NSCollectionViewDropBefore`. You may override this default behavior by changing `proposedDropOperation` or `proposedDropIndex`.

To receive drag messages, you must first send [`registerForDraggedTypes(_:)`](../nsview/registerfordraggedtypes%28_%29.md) to the collection view with the drag types you want to support.

You must implement this method for your collection view to be a drag destination.

## Parameters

- `collectionView`: The collection view that send the message.
- `draggingInfo`: An object containing details about this dragging operation.
- `proposedDropIndex`: The proposed drop index. This parameter is passed by-reference and can be modified retarget the drop operation.
- `proposedDropOperation`: The proposed drop operation. This parameter is passed by-reference and can be modified to change the drop operation.

## See Also

### Legacy Collection View Support
- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
- [func collectionView(NSCollectionView, writeItemsAt: IndexSet, to: NSPasteboard) -> Bool](./collectionview%28_,writeitemsat,to%29-a1lk.md)
  Invoked after it has been determined that a drag should begin, but before the drag has been started.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: IndexSet) -> [String]](./collectionview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditemsat%29-wwec.md)
  Invoked to return an array of filenames that the receiver promises to create.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-4yvk5.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: IndexSet)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-cpuq.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](./collectionview%28_,acceptdrop,index,dropoperation%29.md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:validatedrop:proposedindex:dropoperation:))*
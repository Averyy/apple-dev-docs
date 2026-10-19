# item(at:)

**Framework**: AppKit  
**Kind**: method

Returns the collection view item for the represented object at the specified index.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func item(at index: Int) -> NSCollectionViewItem?
```

#### Return Value

An instance of `NSCollectionViewItem`.

#### Discussion

Rather than using the [`NSCollectionViewItem`](nscollectionviewitem.md) instance returned by this method to determine the frame of the collection item’s view you should use [`content`](nscollectionview/content.md), it is significantly more efficient.

## Parameters

- `index`: The index of the collection view item.

## See Also

- [var selectionIndexes: IndexSet](nscollectionview/selectionindexes.md)
  The indexes of the currently selected items.
- [func frameForItem(at: Int) -> NSRect](nscollectionview/frameforitem(at:).md)
  Returns the frame of the collection view item at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](nscollectionview/frameforitem(at:withnumberofitems:).md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nscollectionview/setdraggingsourceoperationmask(_:forlocal:).md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/item(at:)-80xze)*
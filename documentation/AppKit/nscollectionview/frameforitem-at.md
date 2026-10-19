# frameForItem(at:)

**Framework**: AppKit  
**Kind**: method

Returns the frame of the collection view item at the specified index.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func frameForItem(at index: Int) -> NSRect
```

#### Return Value

The frame calculated by the receiver where it intends to place the subview for the [`NSCollectionViewItem`](nscollectionviewitem.md) at the given index. The rectangle is returned in the collection view’s coordinate system.

#### Discussion

You can use this method in the [`collectionView(_:draggingImageForItemsAt:with:offset:)`](nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-4yvk5.md) method to determine which views are in the visible portion of the enclosing scroll view.

Overriding this method will have no effect on the collection view’s subview layout.

## Parameters

- `index`: The index of the collection view item.

## See Also

- [var selectionIndexes: IndexSet](nscollectionview/selectionindexes.md)
  The indexes of the currently selected items.
- [func item(at: Int) -> NSCollectionViewItem?](nscollectionview/item(at:)-80xze.md)
  Returns the collection view item for the represented object at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](nscollectionview/frameforitem(at:withnumberofitems:).md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nscollectionview/setdraggingsourceoperationmask(_:forlocal:).md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/frameforitem(at:))*
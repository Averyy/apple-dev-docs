# maxItemSize

**Framework**: AppKit  
**Kind**: property

The maximum size (in points) of items in the collection view grid.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var maxItemSize: NSSize { get set }
```

#### Discussion

Setting the size to (`0`, `0`) means that there is no maximum grid size. The default value of this property is (`0`, `0`). If an item’s view  is resizable, set the value to the maximum size that the view should use.

## See Also

- [var itemPrototype: NSCollectionViewItem?](nscollectionview/itemprototype.md)
  The receiver’s collection view item prototype.
- [func newItem(forRepresentedObject: Any) -> NSCollectionViewItem](nscollectionview/newitem(forrepresentedobject:).md)
  Returns the collection view item that is used for the specified object.
- [var selectionIndexes: IndexSet](nscollectionview/selectionindexes.md)
  The indexes of the currently selected items.
- [var maxNumberOfRows: Int](nscollectionview/maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var maxNumberOfColumns: Int](nscollectionview/maxnumberofcolumns.md)
  The maximum number of columns that the collection view displays.
- [var minItemSize: NSSize](nscollectionview/minitemsize.md)
  The minimum size (in points) of items in the collection view grid.
- [func item(at: Int) -> NSCollectionViewItem?](nscollectionview/item(at:)-80xze.md)
  Returns the collection view item for the represented object at the specified index.
- [func frameForItem(at: Int) -> NSRect](nscollectionview/frameforitem(at:).md)
  Returns the frame of the collection view item at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](nscollectionview/frameforitem(at:withnumberofitems:).md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nscollectionview/setdraggingsourceoperationmask(_:forlocal:).md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/maxitemsize)*
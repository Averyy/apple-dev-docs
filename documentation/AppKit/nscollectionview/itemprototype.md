# itemPrototype

**Framework**: AppKit  
**Kind**: property

The receiver’s collection view item prototype.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var itemPrototype: NSCollectionViewItem? { get set }
```

#### Discussion

Whenever possible, use a data source object to provide items. For more information, see the [`dataSource`](nscollectionview/datasource.md) property.

## See Also

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
- [var maxItemSize: NSSize](nscollectionview/maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/itemprototype)*
# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method

Configures the default value returned from [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/objectivec/nsobject/1415984-draggingsourceoperationmaskforlo).

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func setDraggingSourceOperationMask(_ dragOperationMask: NSDragOperation, forLocal localDestination: Bool)
```

#### Discussion

By default, this method returns [`every`](nsdragoperation/every.md) when `localDestination` is [`true`](https://developer.apple.com/documentation/swift/true) and [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md) when `localDestination` is [`false`](https://developer.apple.com/documentation/swift/false). `NSCollectionView` will save the values you set for each `localDestination` value.

You typically will invoke this method, and not override it.

## Parameters

- `dragOperationMask`: The types of drag operations allowed.
- `localDestination`: If  , mask applies when the drag destination object is in the same application as the receiver; if  , mask applies when the destination object is outside the receiver’s application.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/setdraggingsourceoperationmask(_:forlocal:))*
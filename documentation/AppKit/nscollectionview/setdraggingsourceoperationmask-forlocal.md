# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method

Configures the drag operation mask.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setDraggingSourceOperationMask(_ dragOperationMask: NSDragOperation, forLocal localDestination: Bool)
```

#### Discussion

This method configures the default value returned from [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/draggingsourceoperationmaskforlocal:). By default, this method returns [`every`](nsdragoperation/every.md) when `localDestination` is [`true`](https://developer.apple.com/documentation/swift/true) and [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md) when `localDestination` is [`false`](https://developer.apple.com/documentation/swift/false). `NSCollectionView` will save the values you set for each `localDestination` value.

You typically will invoke this method, and not override it.

## Parameters

- `dragOperationMask`: The types of drag operations allowed.
- `localDestination`: If [`true`](https://developer.apple.com/documentation/swift/true), mask applies when the drag destination object is in the same application as the receiver; if [`false`](https://developer.apple.com/documentation/swift/false), mask applies when the destination object is outside the receiver’s application.

## See Also

- [var selectionIndexes: IndexSet](nscollectionview/selectionindexes.md)
  The indexes of the currently selected items.
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
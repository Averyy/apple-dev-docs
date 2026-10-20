# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Configures the drag operation mask.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setDraggingSourceOperationMask(_ dragOperationMask: NSDragOperation, forLocal localDestination: Bool)
```

```objc
- (void) setDraggingSourceOperationMask:(NSDragOperation) dragOperationMask forLocal:(BOOL) localDestination;
```

#### Discussion

This method configures the default value returned from [`draggingSourceOperationMaskForLocal:`](../../ObjectiveC/nsobject-swift.class/draggingsourceoperationmaskforlocal_.md). By default, this method returns [`every`](../nsdragoperation/every.md) when `localDestination` is [`true`](../../Swift/true.md) and [`NSDragOperationNone`](../nsdragoperation/nsdragoperationnone.md) when `localDestination` is [`false`](../../Swift/false.md). `NSCollectionView` will save the values you set for each `localDestination` value.

You typically will invoke this method, and not override it.

## Parameters

- `dragOperationMask`: The types of drag operations allowed.
- `localDestination`: If [`true`](../../Swift/true.md), mask applies when the drag destination object is in the same application as the receiver; if [`false`](../../Swift/false.md), mask applies when the destination object is outside the receiver’s application.

## See Also

### Legacy Collection View Support
- [var selectionIndexes: IndexSet](./selectionindexes.md)
  The indexes of the currently selected items.
- [func item(at: Int) -> NSCollectionViewItem?](./item%28at%29-80xze.md)
  Returns the collection view item for the represented object at the specified index.
- [func frameForItem(at: Int) -> NSRect](./frameforitem%28at%29.md)
  Returns the frame of the collection view item at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](./frameforitem%28at,withnumberofitems%29.md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./draggingimageforitems%28at,with,offset%29-951w7.md)
  This method computes and returns an image to use for dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/setdraggingsourceoperationmask(_:forlocal:))*
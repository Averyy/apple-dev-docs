# setDrop(_:dropOperation:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Allows the class to retarget the drop action.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setDrop(_ index: Int, dropOperation operation: IKImageBrowserDropOperation)
```

```objc
- (void) setDropIndex:(NSInteger) index dropOperation:(IKImageBrowserDropOperation) operation;
```

#### Discussion

For example, To specify a drop on the second item, one would specify index as `1`, and operation as [`IKImageBrowserDropOn`](../ikimagebrowserdropon.md). To specify a drop after the last item, one would specify index as the number of items and operation as [`IKImageBrowserDropBefore`](../ikimagebrowserdropbefore.md).

Passing a value of `–1` for `index`, and [`IKImageBrowserDropOn`](../ikimagebrowserdropon.md) as the operation causes the entire browser view to be highlighted rather than a specific item. This is useful if the data displayed by the receiver does not allow the user to drop items at a specific item location

.

## Parameters

- `index`: The requested drop index.
- `operation`: The requested drop operation. The possible values are described in [`IKImageBrowserDropOperation`](../ikimagebrowserdropoperation.md).

## See Also

### Supporting Drag and Drop
- [func setDraggingDestinationDelegate(Any!)](./setdraggingdestinationdelegate%28_%29.md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](./draggingdestinationdelegate%28%29.md)
  Returns the dragging destination delegate of the receiver.
- [func indexAtLocationOfDroppedItem() -> Int](./indexatlocationofdroppeditem%28%29.md)
  Returns the index of the cell where the drop operation occurred.
- [func setAllowsDroppingOnItems(Bool)](./setallowsdroppingonitems%28_%29.md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](./allowsdroppingonitems%28%29.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](./dropoperation%28%29.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setdrop(_:dropoperation:))*
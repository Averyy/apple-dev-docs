# dropOperation()

**Framework**: Quartz  
**Kind**: method

Returns the current drop operation.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func dropOperation() -> IKImageBrowserDropOperation
```

#### Return Value

[`IKImageBrowserDropOn`](ikimagebrowserdropon.md) if the drop occurs on an item, otherwise [`IKImageBrowserDropBefore`](ikimagebrowserdropbefore.md).

#### Discussion

The returned value is valid when a drop occurred and until next drop.

For example, given a browser with `N` cells , a cell of `N-1` and operation of [`IKImageBrowserDropOn`](ikimagebrowserdropon.md) would specify a drop on the last cell.  To specify a drop after the last cell, one would use an index of `N` and [`IKImageBrowserDropBefore`](ikimagebrowserdropbefore.md) for the operation.

## See Also

- [func setDraggingDestinationDelegate(Any!)](ikimagebrowserview/setdraggingdestinationdelegate(_:).md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](ikimagebrowserview/draggingdestinationdelegate.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](ikimagebrowserview/setdrop(_:dropoperation:).md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](ikimagebrowserview/indexatlocationofdroppeditem.md)
  Returns the index of the cell where the drop operation occurred.
- [func setAllowsDroppingOnItems(Bool)](ikimagebrowserview/setallowsdroppingonitems(_:).md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](ikimagebrowserview/allowsdroppingonitems.md)
  Returns whether the user can drop on items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/dropoperation())*
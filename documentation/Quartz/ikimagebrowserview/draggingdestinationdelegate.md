# draggingDestinationDelegate()

**Framework**: Quartz  
**Kind**: method

Returns the dragging destination delegate of the receiver.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func draggingDestinationDelegate() -> Any!
```

#### Return Value

The receiver’s dragging destination delegate.

## See Also

- [func setDraggingDestinationDelegate(Any!)](ikimagebrowserview/setdraggingdestinationdelegate(_:).md)
  Sets the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](ikimagebrowserview/setdrop(_:dropoperation:).md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](ikimagebrowserview/indexatlocationofdroppeditem.md)
  Returns the index of the cell where the drop operation occurred.
- [func setAllowsDroppingOnItems(Bool)](ikimagebrowserview/setallowsdroppingonitems(_:).md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](ikimagebrowserview/allowsdroppingonitems.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](ikimagebrowserview/dropoperation.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/draggingdestinationdelegate())*
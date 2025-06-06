# indexAtLocationOfDroppedItem()

**Framework**: Quartz  
**Kind**: method

Returns the index of the cell where the drop operation occurred.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func indexAtLocationOfDroppedItem() -> Int
```

#### Return Value

The index of the cell where the drop operation occurred.

#### Discussion

The returned index is valid until the next drop occurs.

## See Also

- [func setDraggingDestinationDelegate(Any!)](ikimagebrowserview/setdraggingdestinationdelegate(_:).md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](ikimagebrowserview/draggingdestinationdelegate.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](ikimagebrowserview/setdrop(_:dropoperation:).md)
  Allows the class to retarget the drop action.
- [func setAllowsDroppingOnItems(Bool)](ikimagebrowserview/setallowsdroppingonitems(_:).md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](ikimagebrowserview/allowsdroppingonitems.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](ikimagebrowserview/dropoperation.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/indexatlocationofdroppeditem())*
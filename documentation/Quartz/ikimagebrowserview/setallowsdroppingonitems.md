# setAllowsDroppingOnItems(_:)

**Framework**: Quartz  
**Kind**: method

Specifies whether the user can drop on items.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setAllowsDroppingOnItems(_ flag: Bool)
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `flag`:   if the user is able to drop on items, otherwise  .

## See Also

- [func setDraggingDestinationDelegate(Any!)](ikimagebrowserview/setdraggingdestinationdelegate(_:).md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](ikimagebrowserview/draggingdestinationdelegate.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](ikimagebrowserview/setdrop(_:dropoperation:).md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](ikimagebrowserview/indexatlocationofdroppeditem.md)
  Returns the index of the cell where the drop operation occurred.
- [func allowsDroppingOnItems() -> Bool](ikimagebrowserview/allowsdroppingonitems.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](ikimagebrowserview/dropoperation.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setallowsdroppingonitems(_:))*
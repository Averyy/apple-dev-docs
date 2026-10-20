# indexAtLocationOfDroppedItem()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the index of the cell where the drop operation occurred.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func indexAtLocationOfDroppedItem() -> Int
```

```objc
- (NSUInteger) indexAtLocationOfDroppedItem;
```

#### Return Value

The index of the cell where the drop operation occurred.

#### Discussion

The returned index is valid until the next drop occurs.

## See Also

### Supporting Drag and Drop
- [func setDraggingDestinationDelegate(Any!)](./setdraggingdestinationdelegate%28_%29.md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](./draggingdestinationdelegate%28%29.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](./setdrop%28_,dropoperation%29.md)
  Allows the class to retarget the drop action.
- [func setAllowsDroppingOnItems(Bool)](./setallowsdroppingonitems%28_%29.md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](./allowsdroppingonitems%28%29.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](./dropoperation%28%29.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/indexatlocationofdroppeditem())*
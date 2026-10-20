# draggingDestinationDelegate()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the dragging destination delegate of the receiver.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func draggingDestinationDelegate() -> Any!
```

```objc
- (id) draggingDestinationDelegate;
```

#### Return Value

The receiver’s dragging destination delegate.

## See Also

### Supporting Drag and Drop
- [func setDraggingDestinationDelegate(Any!)](./setdraggingdestinationdelegate%28_%29.md)
  Sets the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](./setdrop%28_,dropoperation%29.md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](./indexatlocationofdroppeditem%28%29.md)
  Returns the index of the cell where the drop operation occurred.
- [func setAllowsDroppingOnItems(Bool)](./setallowsdroppingonitems%28_%29.md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](./allowsdroppingonitems%28%29.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](./dropoperation%28%29.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/draggingdestinationdelegate())*
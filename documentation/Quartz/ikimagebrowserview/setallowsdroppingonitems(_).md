# setAllowsDroppingOnItems(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Specifies whether the user can drop on items.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setAllowsDroppingOnItems(_ flag: Bool)
```

```objc
- (void) setAllowsDroppingOnItems:(BOOL) flag;
```

#### Discussion

The default is [`false`](../../Swift/false.md).

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the user is able to drop on items, otherwise [`false`](../../Swift/false.md).

## See Also

### Supporting Drag and Drop
- [func setDraggingDestinationDelegate(Any!)](./setdraggingdestinationdelegate%28_%29.md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](./draggingdestinationdelegate%28%29.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](./setdrop%28_,dropoperation%29.md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](./indexatlocationofdroppeditem%28%29.md)
  Returns the index of the cell where the drop operation occurred.
- [func allowsDroppingOnItems() -> Bool](./allowsdroppingonitems%28%29.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](./dropoperation%28%29.md)
  Returns the current drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setallowsdroppingonitems(_:))*
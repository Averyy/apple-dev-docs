# shouldCollapseAutoExpandedItems(forDeposited:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether auto-expanded items should return to their original collapsed state.

**Availability**:
- macOS

## Declaration

```swift
func shouldCollapseAutoExpandedItems(forDeposited deposited: Bool) -> Bool
```

```objc
- (BOOL) shouldCollapseAutoExpandedItemsForDeposited:(BOOL) deposited;
```

## Return Value

[`true`](../../Swift/true.md) if auto-expanded items should return to their original collapsed state; otherwise [`false`](../../Swift/false.md).

## Discussion

Override this method to provide custom behavior. If the target of a drop is not auto-expanded (by hovering long enough) the drop target still gets expanded after a successful drop unless this method returns [`true`](../../Swift/true.md). The default implementation returns [`false`](../../Swift/false.md) after a successful drop.

This method is called in a variety of situations. For example, it is called shortly after the [`outlineView(_:acceptDrop:item:childIndex:)`](../nsoutlineviewdatasource/outlineview%28_,acceptdrop,item,childindex%29.md) method is called and also if the drag exits the outline view (exiting the view is treated the same as a failed drop). The return value of the [`outlineView(_:acceptDrop:item:childIndex:)`](../nsoutlineviewdatasource/outlineview%28_,acceptdrop,item,childindex%29.md) method determines the incoming value of the `deposited` parameter.

## Parameters

- `deposited`: If [`true`](../../Swift/true.md), the drop terminated successfully; if [`false`](../../Swift/false.md) the drop failed.

## See Also

### Supporting Drag and Drop
- [func setDropItem(Any?, dropChildIndex: Int)](./setdropitem%28_,dropchildindex%29.md)
  Used to “retarget” a proposed drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/shouldcollapseautoexpandeditems(fordeposited:))*
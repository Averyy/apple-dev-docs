# shouldCollapseAutoExpandedItems(forDeposited:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether auto-expanded items should return to their original collapsed state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldCollapseAutoExpandedItems(forDeposited deposited: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if auto-expanded items should return to their original collapsed state; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Override this method to provide custom behavior. If the target of a drop is not auto-expanded (by hovering long enough) the drop target still gets expanded after a successful drop unless this method returns [`true`](https://developer.apple.com/documentation/swift/true). The default implementation returns [`false`](https://developer.apple.com/documentation/swift/false) after a successful drop.

This method is called in a variety of situations. For example, it is called shortly after the [`outlineView(_:acceptDrop:item:childIndex:)`](nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:).md) method is called and also if the drag exits the outline view (exiting the view is treated the same as a failed drop). The return value of the [`outlineView(_:acceptDrop:item:childIndex:)`](nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:).md) method determines the incoming value of the `deposited` parameter.

## Parameters

- `deposited`: If  , the drop terminated successfully; if   the drop failed.

## See Also

- [func setDropItem(Any?, dropChildIndex: Int)](nsoutlineview/setdropitem(_:dropchildindex:).md)
  Used to “retarget” a proposed drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/shouldcollapseautoexpandeditems(fordeposited:))*
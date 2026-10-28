# removeSplitViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a specified split view item from the split view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func removeSplitViewItem(_ splitViewItem: NSSplitViewItem)
```

```objc
- (void) removeSplitViewItem:(NSSplitViewItem *) splitViewItem;
```

## Discussion

After you remove a split view item, the system adjusts the layout of the split view accordingly.

## Parameters

- `splitViewItem`: The split view item to remove.

  > ❗ **Important**:  If the split view item is `nil` or isn’t in the [`splitViewItems`](./splitviewitems.md) array, the system throws an exception.

## See Also

### Modifying a Split View Controller
- [func addSplitViewItem(NSSplitViewItem)](./addsplitviewitem%28_%29.md)
  Adds a split view item to the end of the array of split view items.
- [func insertSplitViewItem(NSSplitViewItem, at: Int)](./insertsplitviewitem%28_,at%29.md)
  Adds a split view item to the array of split view items at the specified index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/removesplitviewitem(_:))*
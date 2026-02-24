# insertSplitViewItem(_:at:)

**Framework**: AppKit  
**Kind**: method

Adds a split view item to the array of split view items at the specified index position.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func insertSplitViewItem(_ splitViewItem: NSSplitViewItem, at index: Int)
```

#### Discussion

If the split view controller’s view finishes loading, and the split view item that you add is visible, the system loads the split view item’s view controller’s view and adds it to the split view.

## Parameters

- `splitViewItem`: The split view item to add. > ❗ **Important**:  Before you add a split view item, it must be non-`nil` and it must have an associated view controller, or the system throws an exception.
- `index`: The index position for adding the split view item in the [`splitViewItems`](nssplitviewcontroller/splitviewitems.md) array. > ❗ **Important**:  If the index value is out of bounds (less than `0` or greater than the count of the array), the system throws an exception.

## See Also

- [func addSplitViewItem(NSSplitViewItem)](nssplitviewcontroller/addsplitviewitem(_:).md)
  Adds a split view item to the end of the array of split view items.
- [func removeSplitViewItem(NSSplitViewItem)](nssplitviewcontroller/removesplitviewitem(_:).md)
  Removes a specified split view item from the split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/insertsplitviewitem(_:at:))*
# addSplitViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Adds a split view item to the end of the array of split view items.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func addSplitViewItem(_ splitViewItem: NSSplitViewItem)
```

#### Discussion

This is a convenience method you can use in place of the [`insertSplitViewItem(_:at:)`](nssplitviewcontroller/insertsplitviewitem(_:at:).md) method when you want to add a split view item to the end of the [`splitViewItems`](nssplitviewcontroller/splitviewitems.md) array. Calling this method implicitly calls the [`insertSplitViewItem(_:at:)`](nssplitviewcontroller/insertsplitviewitem(_:at:).md) method.

If you subclass the [`NSSplitViewController`](nssplitviewcontroller.md) class, don’t call this method in your custom object to add a split view item. Instead, call the [`insertSplitViewItem(_:at:)`](nssplitviewcontroller/insertsplitviewitem(_:at:).md) method directly.

## Parameters

- `splitViewItem`: The split view item to add.

## See Also

- [func insertSplitViewItem(NSSplitViewItem, at: Int)](nssplitviewcontroller/insertsplitviewitem(_:at:).md)
  Adds a split view item to the array of split view items at the specified index position.
- [func removeSplitViewItem(NSSplitViewItem)](nssplitviewcontroller/removesplitviewitem(_:).md)
  Removes a specified split view item from the split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/addsplitviewitem(_:))*
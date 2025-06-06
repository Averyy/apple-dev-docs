# removeSplitViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Removes a specified split view item from the split view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func removeSplitViewItem(_ splitViewItem: NSSplitViewItem)
```

#### Discussion

After you remove a split view item, the system adjusts the layout of the split view accordingly.

## Parameters

- `splitViewItem`: The split view item to remove.

## See Also

- [func addSplitViewItem(NSSplitViewItem)](nssplitviewcontroller/addsplitviewitem(_:).md)
  Adds a split view item to the end of the array of split view items.
- [func insertSplitViewItem(NSSplitViewItem, at: Int)](nssplitviewcontroller/insertsplitviewitem(_:at:).md)
  Adds a split view item to the array of split view items at the specified index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/removesplitviewitem(_:))*
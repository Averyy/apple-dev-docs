# addSplitViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a split view item to the end of the array of split view items.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func addSplitViewItem(_ splitViewItem: NSSplitViewItem)
```

```objc
- (void) addSplitViewItem:(NSSplitViewItem *) splitViewItem;
```

#### Discussion

This is a convenience method you can use in place of the [`insertSplitViewItem(_:at:)`](./insertsplitviewitem%28_,at%29.md) method when you want to add a split view item to the end of the [`splitViewItems`](./splitviewitems.md) array. Calling this method implicitly calls the [`insertSplitViewItem(_:at:)`](./insertsplitviewitem%28_,at%29.md) method.

If you subclass the [`NSSplitViewController`](../nssplitviewcontroller.md) class, don’t call this method in your custom object to add a split view item. Instead, call the [`insertSplitViewItem(_:at:)`](./insertsplitviewitem%28_,at%29.md) method directly.

## Parameters

- `splitViewItem`: The split view item to add.

  > ❗ **Important**:  Before you add a split view item, it must be non-`nil` and it must have an associated view controller, or the system throws an exception.

## See Also

### Modifying a Split View Controller
- [func insertSplitViewItem(NSSplitViewItem, at: Int)](./insertsplitviewitem%28_,at%29.md)
  Adds a split view item to the array of split view items at the specified index position.
- [func removeSplitViewItem(NSSplitViewItem)](./removesplitviewitem%28_%29.md)
  Removes a specified split view item from the split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/addsplitviewitem(_:))*
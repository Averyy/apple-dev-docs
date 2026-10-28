# removeTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified tab view item from the tab view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func removeTabViewItem(_ tabViewItem: NSTabViewItem)
```

```objc
- (void) removeTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Discussion

Use this method to remove a tab view item from the tab view interface. Removing the item removes the corresponding view controller from the tab view controller’s list of child view controllers. If the removed tab view item is currently selected, the tab view controller selects the next item (or the previous item if there is no next item). Removing the last tab view item sets the [`selectedTabViewItemIndex`](./selectedtabviewitemindex.md) property to `-1`.

## Parameters

- `tabViewItem`: The tab view item to remove. If this parameter is `nil` or the item does not belong to the tab view controller, this method throws an exception.

## See Also

### Managing Tab View Items
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](./tabviewitem%28for%29.md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](./addtabviewitem%28_%29.md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [var selectedTabViewItemIndex: Int](./selectedtabviewitemindex.md)
  The index of the selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/removetabviewitem(_:))*
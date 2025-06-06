# removeTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified tab view item from the tab view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func removeTabViewItem(_ tabViewItem: NSTabViewItem)
```

#### Discussion

Use this method to remove a tab view item from the tab view interface. Removing the item removes the corresponding view controller from the tab view controller’s list of child view controllers. If the removed tab view item is currently selected, the tab view controller selects the next item (or the previous item if there is no next item). Removing the last tab view item sets the [`selectedTabViewItemIndex`](nstabviewcontroller/selectedtabviewitemindex.md) property to `-1`.

## Parameters

- `tabViewItem`: The tab view item to remove. If this parameter is   or the item does not belong to the tab view controller, this method throws an exception.

## See Also

- [var tabViewItems: [NSTabViewItem]](nstabviewcontroller/tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](nstabviewcontroller/tabviewitem(for:).md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](nstabviewcontroller/addtabviewitem(_:).md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabviewcontroller/inserttabviewitem(_:at:).md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [var selectedTabViewItemIndex: Int](nstabviewcontroller/selectedtabviewitemindex.md)
  The index of the selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/removetabviewitem(_:))*
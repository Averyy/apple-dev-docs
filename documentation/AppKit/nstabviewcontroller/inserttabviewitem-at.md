# insertTabViewItem(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts a tab view into the tab view controller’s list of tabs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func insertTabViewItem(_ tabViewItem: NSTabViewItem, at index: Int)
```

#### Discussion

Use this method to insert new tabs into the existing list of tabs. This method adds the tab’s associated view controller as a child of the tab view controller, so you do not need to call the [`addChild(_:)`](nsviewcontroller/addchild(_:).md) method directly. The view for the new view controller is not loaded until its corresponding tab is selected by the user.

Inserting a new tab updates the tab view interface and adjusts the value in the [`selectedTabViewItemIndex`](nstabviewcontroller/selectedtabviewitemindex.md) property as needed.

If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `tabViewItem`: The tab view item to insert. The tab view item must have an associated view controller. If this parameter is   or if the tab view item does not have a view controller, this method throws an exception.
- `index`: The zero-based index at which to insert the tab. If the index is less than   or greater than the number of items currently in the array, this method raises an exception.

## See Also

- [var tabViewItems: [NSTabViewItem]](nstabviewcontroller/tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](nstabviewcontroller/tabviewitem(for:).md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](nstabviewcontroller/addtabviewitem(_:).md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](nstabviewcontroller/removetabviewitem(_:).md)
  Removes the specified tab view item from the tab view controller.
- [var selectedTabViewItemIndex: Int](nstabviewcontroller/selectedtabviewitemindex.md)
  The index of the selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/inserttabviewitem(_:at:))*
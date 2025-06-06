# tabViewItems

**Framework**: AppKit  
**Kind**: property

The array of tab view items used to manage each of the child view controllers.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var tabViewItems: [NSTabViewItem] { get set }
```

#### Discussion

This property contains an array of [`NSTabViewItem`](nstabviewitem.md) objects. Each tab view item contains information about a tab in the tab view interface, including the child view controller that manages the tab’s contents.

Assigning a new array to this property updates the set of tabs displayed by the tab view controller.

## See Also

- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](nstabviewcontroller/tabviewitem(for:).md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](nstabviewcontroller/addtabviewitem(_:).md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabviewcontroller/inserttabviewitem(_:at:).md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](nstabviewcontroller/removetabviewitem(_:).md)
  Removes the specified tab view item from the tab view controller.
- [var selectedTabViewItemIndex: Int](nstabviewcontroller/selectedtabviewitemindex.md)
  The index of the selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabviewitems)*
# selectedTabViewItemIndex

**Framework**: AppKit  
**Kind**: property

The index of the selected tab.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var selectedTabViewItemIndex: Int { get set }
```

#### Discussion

Use this property to get and set the selected tab. The property is key-value coding compliant and can be the target of bindings.

## See Also

- [var tabViewItems: [NSTabViewItem]](nstabviewcontroller/tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](nstabviewcontroller/tabviewitem(for:).md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](nstabviewcontroller/addtabviewitem(_:).md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabviewcontroller/inserttabviewitem(_:at:).md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](nstabviewcontroller/removetabviewitem(_:).md)
  Removes the specified tab view item from the tab view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/selectedtabviewitemindex)*
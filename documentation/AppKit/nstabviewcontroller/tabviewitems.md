# tabViewItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of tab view items used to manage each of the child view controllers.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var tabViewItems: [NSTabViewItem] { get set }
```

```objc
@property (copy) NSArray<__kindof NSTabViewItem *> * tabViewItems;
```

## Discussion

This property contains an array of [`NSTabViewItem`](../nstabviewitem.md) objects. Each tab view item contains information about a tab in the tab view interface, including the child view controller that manages the tab’s contents.

Assigning a new array to this property updates the set of tabs displayed by the tab view controller.

## See Also

### Managing Tab View Items
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](./tabviewitem%28for%29.md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](./addtabviewitem%28_%29.md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](./removetabviewitem%28_%29.md)
  Removes the specified tab view item from the tab view controller.
- [var selectedTabViewItemIndex: Int](./selectedtabviewitemindex.md)
  The index of the selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabviewitems)*
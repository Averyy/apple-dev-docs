# tabViewItem(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the tab view item for the specified child view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func tabViewItem(for viewController: NSViewController) -> NSTabViewItem?
```

```objc
- (NSTabViewItem *) tabViewItemForViewController:(NSViewController *) viewController;
```

#### Return Value

The tab view item associated with the view controller or `nil` if the view controller is not managed by the tab view controller.

#### Discussion

This method is a convenient way to map a tab view item to a newly added child view controller. When you add child view controllers using the [`addChild(_:)`](../nsviewcontroller/addchild%28_%29.md) method, the tab view automatically controller creates a new tab view item. Use this method to fetch that tab view item and configure it.

## Parameters

- `viewController`: The child view controller whose tab view item you want.

## See Also

### Managing Tab View Items
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func addTabViewItem(NSTabViewItem)](./addtabviewitem%28_%29.md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](./removetabviewitem%28_%29.md)
  Removes the specified tab view item from the tab view controller.
- [var selectedTabViewItemIndex: Int](./selectedtabviewitemindex.md)
  The index of the selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabviewitem(for:))*
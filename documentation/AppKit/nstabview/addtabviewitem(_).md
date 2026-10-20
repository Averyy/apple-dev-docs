# addTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified tab item.

**Availability**:
- macOS

## Declaration

```swift
func addTabViewItem(_ tabViewItem: NSTabViewItem)
```

```objc
- (void) addTabViewItem:(NSTabViewItem *) tabViewItem;
```

#### Discussion

The item is added at the end of the array of tab items, so the new tab appears on the right side of the view. If the delegate supports it, it invokes the delegate’s [`tabViewDidChangeNumberOfTabViewItems(_:)`](../nstabviewdelegate/tabviewdidchangenumberoftabviewitems%28_%29.md) method.

## Parameters

- `tabViewItem`: The tab view item to be added.

## See Also

### Related Documentation
- [Tab View Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/TabView.html#//apple_ref/doc/uid/10000074i)
- [func tabViewItem(at: Int) -> NSTabViewItem](./tabviewitem%28at%29-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var numberOfTabViewItems: Int](./numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The tab view’s array of tab view items.
### Adding and Removing Tabs
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func removeTabViewItem(NSTabViewItem)](./removetabviewitem%28_%29.md)
  Removes the specified item from the tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/addtabviewitem(_:))*
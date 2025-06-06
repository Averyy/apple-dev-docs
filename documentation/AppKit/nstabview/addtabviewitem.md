# addTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Adds the specified tab item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addTabViewItem(_ tabViewItem: NSTabViewItem)
```

#### Discussion

The item is added at the end of the array of tab items, so the new tab appears on the right side of the view. If the delegate supports it, it invokes the delegate’s [`tabViewDidChangeNumberOfTabViewItems(_:)`](nstabviewdelegate/tabviewdidchangenumberoftabviewitems(_:).md) method.

## Parameters

- `tabViewItem`: The tab view item to be added.

## See Also

- [Tab View Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/TabView.html#//apple_ref/doc/uid/10000074i)
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func removeTabViewItem(NSTabViewItem)](nstabview/removetabviewitem(_:).md)
  Removes the specified item from the tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/addtabviewitem(_:))*
# insertTabViewItem(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts the specified item into the tab view’s array of tab view items at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertTabViewItem(_ tabViewItem: NSTabViewItem, at index: Int)
```

#### Discussion

If there is a delegate and the delegate supports it, sends the delegate the [`tabViewDidChangeNumberOfTabViewItems(_:)`](nstabviewdelegate/tabviewdidchangenumberoftabviewitems(_:).md) message.

## Parameters

- `tabViewItem`: The tab view item to be added.
- `index`: The index at which to insert the tab view item. The   parameter is zero-based.

## See Also

- [func indexOfTabViewItem(withIdentifier: Any) -> Int](nstabview/indexoftabviewitem(withidentifier:).md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func indexOfTabViewItem(NSTabViewItem) -> Int](nstabview/indexoftabviewitem(_:).md)
  Returns the index of the specified item in the tab view.
- [func addTabViewItem(NSTabViewItem)](nstabview/addtabviewitem(_:).md)
  Adds the specified tab item.
- [func removeTabViewItem(NSTabViewItem)](nstabview/removetabviewitem(_:).md)
  Removes the specified item from the tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/inserttabviewitem(_:at:))*
# removeTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified item from the tab view’s array of tab view items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeTabViewItem(_ tabViewItem: NSTabViewItem)
```

#### Discussion

If there is a delegate and the delegate supports it, sends the delegate the [`tabViewDidChangeNumberOfTabViewItems(_:)`](nstabviewdelegate/tabviewdidchangenumberoftabviewitems(_:).md) message.

## Parameters

- `tabViewItem`: The tab view item to be removed.

## See Also

- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.
- [func addTabViewItem(NSTabViewItem)](nstabview/addtabviewitem(_:).md)
  Adds the specified tab item.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/removetabviewitem(_:))*
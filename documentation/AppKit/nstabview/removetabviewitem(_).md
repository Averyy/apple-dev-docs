# removeTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified item from the tab view’s array of tab view items.

**Availability**:
- macOS

## Declaration

```swift
func removeTabViewItem(_ tabViewItem: NSTabViewItem)
```

```objc
- (void) removeTabViewItem:(NSTabViewItem *) tabViewItem;
```

#### Discussion

If there is a delegate and the delegate supports it, sends the delegate the [`tabViewDidChangeNumberOfTabViewItems(_:)`](../nstabviewdelegate/tabviewdidchangenumberoftabviewitems%28_%29.md) message.

## Parameters

- `tabViewItem`: The tab view item to be removed.

## See Also

### Related Documentation
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The tab view’s array of tab view items.
### Adding and Removing Tabs
- [func addTabViewItem(NSTabViewItem)](./addtabviewitem%28_%29.md)
  Adds the specified tab item.
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/removetabviewitem(_:))*
# indexOfTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the specified item in the tab view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfTabViewItem(_ tabViewItem: NSTabViewItem) -> Int
```

#### Return Value

The zero-based index of `tabViewItem`, or `NSNotFound` if the item is not found.

#### Discussion

The returned index is zero-based.

## Parameters

- `tabViewItem`: The tab view item.

## See Also

- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](nstabview/indexoftabviewitem(withidentifier:).md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/indexoftabviewitem(_:))*
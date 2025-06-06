# tabViewItem(at:)

**Framework**: AppKit  
**Kind**: method

Returns the tab view item at `index` in the tab view’s array of items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tabViewItem(at index: Int) -> NSTabViewItem
```

#### Return Value

The tab view item at the specified index.

## Parameters

- `index`: The index at which to insert the tab view item. The   parameter is zero-based.

## See Also

- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func indexOfTabViewItem(NSTabViewItem) -> Int](nstabview/indexoftabviewitem(_:).md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](nstabview/indexoftabviewitem(withidentifier:).md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewitem(at:)-7r3at)*
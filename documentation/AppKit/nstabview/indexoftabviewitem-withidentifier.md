# indexOfTabViewItem(withIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfTabViewItem(withIdentifier identifier: Any) -> Int
```

#### Return Value

The zero-based index of the tab view item corresponding to `identifier`, or `NSNotFound` if the item is not found.

#### Discussion

The returned index is zero-based.

## Parameters

- `identifier`: The identifier of a tab view item.

## See Also

- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func indexOfTabViewItem(NSTabViewItem) -> Int](nstabview/indexoftabviewitem(_:).md)
  Returns the index of the specified item in the tab view.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/indexoftabviewitem(withidentifier:))*
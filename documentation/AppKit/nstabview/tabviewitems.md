# tabViewItems

**Framework**: AppKit  
**Kind**: property

The tab view’s array of tab view items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var tabViewItems: [NSTabViewItem] { get set }
```

#### Discussion

A tab view keeps an array containing one tab view item for each tab in the view. The default value of this property is an empty array.

## See Also

- [func indexOfTabViewItem(NSTabViewItem) -> Int](nstabview/indexoftabviewitem(_:).md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](nstabview/indexoftabviewitem(withidentifier:).md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewitems)*
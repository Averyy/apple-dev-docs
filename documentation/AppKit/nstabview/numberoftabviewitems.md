# numberOfTabViewItems

**Framework**: AppKit  
**Kind**: property

The number of items in the tab view’s array of tab view items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfTabViewItems: Int { get }
```

#### Discussion

The default value of this property is 0.

## See Also

- [func indexOfTabViewItem(NSTabViewItem) -> Int](nstabview/indexoftabviewitem(_:).md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](nstabview/indexoftabviewitem(withidentifier:).md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/numberoftabviewitems)*
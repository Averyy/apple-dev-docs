# indexOfTabViewItem(withIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.

**Availability**:
- macOS

## Declaration

```swift
func indexOfTabViewItem(withIdentifier identifier: Any) -> Int
```

```objc
- (NSInteger) indexOfTabViewItemWithIdentifier:(id) identifier;
```

#### Return Value

The zero-based index of the tab view item corresponding to `identifier`, or `NSNotFound` if the item is not found.

#### Discussion

The returned index is zero-based.

## Parameters

- `identifier`: The identifier of a tab view item.

## See Also

### Related Documentation
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
### Accessing Tabs
- [func indexOfTabViewItem(NSTabViewItem) -> Int](./indexoftabviewitem%28_%29.md)
  Returns the index of the specified item in the tab view.
- [var numberOfTabViewItems: Int](./numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](./tabviewitem%28at%29-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/indexoftabviewitem(withidentifier:))*
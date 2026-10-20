# tabViewItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the tab view item at `index` in the tab view’s array of items.

**Availability**:
- macOS

## Declaration

```swift
func tabViewItem(at index: Int) -> NSTabViewItem
```

```objc
- (NSTabViewItem *) tabViewItemAtIndex:(NSInteger) index;
```

#### Return Value

The tab view item at the specified index.

## Parameters

- `index`: The index at which to insert the tab view item. The `index` parameter is zero-based.

## See Also

### Related Documentation
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
### Accessing Tabs
- [func indexOfTabViewItem(NSTabViewItem) -> Int](./indexoftabviewitem%28_%29.md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](./indexoftabviewitem%28withidentifier%29.md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](./numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewitem(at:)-7r3at)*
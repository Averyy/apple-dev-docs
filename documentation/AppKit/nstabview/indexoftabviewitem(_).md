# indexOfTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the specified item in the tab view.

**Availability**:
- macOS

## Declaration

```swift
func indexOfTabViewItem(_ tabViewItem: NSTabViewItem) -> Int
```

```objc
- (NSInteger) indexOfTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Return Value

The zero-based index of `tabViewItem`, or `NSNotFound` if the item is not found.

## Discussion

The returned index is zero-based.

## Parameters

- `tabViewItem`: The tab view item.

## See Also

### Related Documentation
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
### Accessing Tabs
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](./indexoftabviewitem%28withidentifier%29.md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](./numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](./tabviewitem%28at%29-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/indexoftabviewitem(_:))*
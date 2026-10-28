# numberOfTabViewItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of items in the tab view’s array of tab view items.

**Availability**:
- macOS

## Declaration

```swift
var numberOfTabViewItems: Int { get }
```

```objc
@property (readonly) NSInteger numberOfTabViewItems;
```

## Discussion

The default value of this property is 0.

## See Also

### Accessing Tabs
- [func indexOfTabViewItem(NSTabViewItem) -> Int](./indexoftabviewitem%28_%29.md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](./indexoftabviewitem%28withidentifier%29.md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [func tabViewItem(at: Int) -> NSTabViewItem](./tabviewitem%28at%29-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/numberoftabviewitems)*
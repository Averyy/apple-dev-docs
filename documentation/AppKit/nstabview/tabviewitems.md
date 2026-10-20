# tabViewItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tab view’s array of tab view items.

**Availability**:
- macOS

## Declaration

```swift
var tabViewItems: [NSTabViewItem] { get set }
```

```objc
@property (copy) NSArray<__kindof NSTabViewItem *> * tabViewItems;
```

#### Discussion

A tab view keeps an array containing one tab view item for each tab in the view. The default value of this property is an empty array.

## See Also

### Accessing Tabs
- [func indexOfTabViewItem(NSTabViewItem) -> Int](./indexoftabviewitem%28_%29.md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](./indexoftabviewitem%28withidentifier%29.md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](./numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](./tabviewitem%28at%29-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewitems)*
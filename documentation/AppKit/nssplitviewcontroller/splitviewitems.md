# splitViewItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of split view items that correspond to the split view controller’s child view controllers.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var splitViewItems: [NSSplitViewItem] { get set }
```

```objc
@property (copy) NSArray<__kindof NSSplitViewItem *> * splitViewItems;
```

#### Discussion

Setting this property implicitly calls the [`insertSplitViewItem(_:at:)`](./insertsplitviewitem%28_,at%29.md) or [`removeSplitViewItem(_:)`](./removesplitviewitem%28_%29.md) method, as appropriate, to add or remove split view items from this array.

If you add a child view controller to the split view controller, the system automatically creates a default split view item for the child view controller and adds it to the [`splitViewItems`](./splitviewitems.md) array.

If you remove a child view controller, the split view controller removes its corresponding split view item from the [`splitViewItems`](./splitviewitems.md) array.

## See Also

### Configuring and Managing a Split View Controller
- [var splitView: NSSplitView](./splitview.md)
  The split view that the split view controller manages.
- [func splitViewItem(for: NSViewController) -> NSSplitViewItem?](./splitviewitem%28for%29.md)
  Returns the corresponding split view item for the specified child view controller of the split view controller.
- [class NSSplitViewItem](../nssplitviewitem.md)
  An item in a split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitviewitems)*
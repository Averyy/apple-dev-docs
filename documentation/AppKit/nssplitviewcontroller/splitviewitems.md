# splitViewItems

**Framework**: AppKit  
**Kind**: property

The array of split view items that correspond to the split view controller’s child view controllers.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var splitViewItems: [NSSplitViewItem] { get set }
```

#### Discussion

Setting this property implicitly calls the [`insertSplitViewItem(_:at:)`](nssplitviewcontroller/insertsplitviewitem(_:at:).md) or [`removeSplitViewItem(_:)`](nssplitviewcontroller/removesplitviewitem(_:).md) method, as appropriate, to add or remove split view items from this array.

If you add a child view controller to the split view controller, the system automatically creates a default split view item for the child view controller and adds it to the [`splitViewItems`](nssplitviewcontroller/splitviewitems.md) array.

If you remove a child view controller, the split view controller removes its corresponding split view item from the [`splitViewItems`](nssplitviewcontroller/splitviewitems.md) array.

## See Also

- [var splitView: NSSplitView](nssplitviewcontroller/splitview.md)
  The split view that the split view controller manages.
- [func splitViewItem(for: NSViewController) -> NSSplitViewItem?](nssplitviewcontroller/splitviewitem(for:).md)
  Returns the corresponding split view item for the specified child view controller of the split view controller.
- [class NSSplitViewItem](nssplitviewitem.md)
  An item in a split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitviewitems)*
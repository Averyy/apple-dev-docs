# splitView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The split view that the split view controller manages.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var splitView: NSSplitView { get set }
```

```objc
@property (strong) NSSplitView * splitView;
```

#### Discussion

This property gives you access to the split view controller’s split view for querying its attributes or customizing it.

By default, a split view arranges its child views vertically from top to bottom. To specify a horizontal (side-by-side) arrangement, implement the [`isVertical`](../nssplitview/isvertical.md) property of the split view object to return [`true`](../../Swift/true.md).

Also by default, a split view has a divider style of [`NSSplitView.DividerStyle.thin`](../nssplitview/dividerstyle-swift.enum/thin.md), and doesn’t have an autosave name.

> ❗ **Important**:  Don’t change the [`delegate`](../nssplitview/delegate.md) property of a split view through the [`splitView`](./splitview.md) property of a split view controller, and don’t call any methods on the split view object using this property. If you do, the system raises an exception.

To provide a custom split view, set this property at any time before you call `super` in the inherited [`viewDidLoad()`](../nsviewcontroller/viewdidload%28%29.md) method; that is, before the split view controller’s [`isViewLoaded`](../nsviewcontroller/isviewloaded.md) property is [`true`](../../Swift/true.md).

The split view isn’t always the same object as that in the split view controller’s inherited [`view`](../nsviewcontroller/view.md) property. To access the split view, always use the [`splitView`](./splitview.md) property.

## See Also

### Configuring and Managing a Split View Controller
- [func splitViewItem(for: NSViewController) -> NSSplitViewItem?](./splitviewitem%28for%29.md)
  Returns the corresponding split view item for the specified child view controller of the split view controller.
- [var splitViewItems: [NSSplitViewItem]](./splitviewitems.md)
  The array of split view items that correspond to the split view controller’s child view controllers.
- [class NSSplitViewItem](../nssplitviewitem.md)
  An item in a split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview)*
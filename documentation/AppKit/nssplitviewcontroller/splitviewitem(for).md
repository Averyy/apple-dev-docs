# splitViewItem(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the corresponding split view item for the specified child view controller of the split view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func splitViewItem(for viewController: NSViewController) -> NSSplitViewItem?
```

```objc
- (NSSplitViewItem *) splitViewItemForViewController:(NSViewController *) viewController;
```

## Return Value

The corresponding split view item, or `nil` if `viewController` isn’t a child of the split view controller.

## Parameters

- `viewController`: The child view controller with the corresponding split view item you want.

## See Also

### Configuring and Managing a Split View Controller
- [var splitView: NSSplitView](./splitview.md)
  The split view that the split view controller manages.
- [var splitViewItems: [NSSplitViewItem]](./splitviewitems.md)
  The array of split view items that correspond to the split view controller’s child view controllers.
- [class NSSplitViewItem](../nssplitviewitem.md)
  An item in a split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitviewitem(for:))*
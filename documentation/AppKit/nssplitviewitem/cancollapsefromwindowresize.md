# canCollapseFromWindowResize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether a window resize can collapse the child view controller that corresponds to the split view item.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var canCollapseFromWindowResize: Bool { get set }
```

```objc
@property BOOL canCollapseFromWindowResize;
```

## Discussion

This can differ from [`canCollapse`](./cancollapse.md) to allow divider collapsing but not windows resize collapsing, or vice versa.

The default value of this property is [`true`](../../Swift/true.md) for Sidebars and [`false`](../../Swift/false.md) for Inspectors.

> **Note**:  Setting `canCollapse` for sidebars resets this value to that new value.

## See Also

### Collapsing and expanding the item
- [var isCollapsed: Bool](./iscollapsed.md)
  A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.
- [var canCollapse: Bool](./cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](./collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [NSSplitViewItem.CollapseBehavior](./collapsebehavior-swift.enum.md)
  Constants that describe the split view item’s collapsing behavior.
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/cancollapsefromwindowresize)*
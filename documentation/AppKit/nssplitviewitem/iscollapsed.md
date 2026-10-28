# isCollapsed

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isCollapsed: Bool { get set }
```

```objc
@property (getter=isCollapsed) BOOL collapsed;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Collapsing and expanding the item
- [var canCollapse: Bool](./cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](./collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [NSSplitViewItem.CollapseBehavior](./collapsebehavior-swift.enum.md)
  Constants that describe the split view item’s collapsing behavior.
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.
- [var canCollapseFromWindowResize: Bool](./cancollapsefromwindowresize.md)
  A Boolean value that determines whether a window resize can collapse the child view controller that corresponds to the split view item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/iscollapsed)*
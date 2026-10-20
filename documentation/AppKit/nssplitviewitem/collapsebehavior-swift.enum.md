# NSSplitViewItem.CollapseBehavior

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the split view item’s collapsing behavior.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum CollapseBehavior
```

```c
enum NSSplitViewItemCollapseBehavior : NSInteger;
```

## Topics

### Constants
- [NSSplitViewItem.CollapseBehavior.default](./collapsebehavior-swift.enum/default.md)
  The item uses the default collapsing behavior.
- [NSSplitViewItem.CollapseBehavior.preferResizingSplitViewWithFixedSiblings](./collapsebehavior-swift.enum/preferresizingsplitviewwithfixedsiblings.md)
  The item’s preference is to keep the other panes at their current size and position onscreen, potentially growing or shrinking the window in the direction to best preserve that.
- [NSSplitViewItem.CollapseBehavior.preferResizingSiblingsWithFixedSplitView](./collapsebehavior-swift.enum/preferresizingsiblingswithfixedsplitview.md)
  The item’s preference is to resize the other split panes.
- [NSSplitViewItem.CollapseBehavior.useConstraints](./collapsebehavior-swift.enum/useconstraints.md)
  The item collapses and expands using a constraint animation, with a constraint priority of the item’s holding priority.
### Initializers
- [init?(rawValue: Int)](./collapsebehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Collapsing and expanding the item
- [var isCollapsed: Bool](./iscollapsed.md)
  A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.
- [var canCollapse: Bool](./cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](./collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.
- [var canCollapseFromWindowResize: Bool](./cancollapsefromwindowresize.md)
  A Boolean value that determines whether a window resize can collapse the child view controller that corresponds to the split view item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.enum)*
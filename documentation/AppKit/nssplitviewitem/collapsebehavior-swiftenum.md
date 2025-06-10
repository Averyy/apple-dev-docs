# NSSplitViewItem.CollapseBehavior

**Framework**: AppKit  
**Kind**: enum

Constants that describe the split view item’s collapsing behavior.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum CollapseBehavior
```

## Topics

### Constants
- [NSSplitViewItem.CollapseBehavior.default](nssplitviewitem/collapsebehavior-swift.enum/default.md)
  The item uses the default collapsing behavior.
- [NSSplitViewItem.CollapseBehavior.preferResizingSplitViewWithFixedSiblings](nssplitviewitem/collapsebehavior-swift.enum/preferresizingsplitviewwithfixedsiblings.md)
  The item’s preference is to keep the other panes at their current size and position onscreen, potentially growing or shrinking the window in the direction to best preserve that.
- [NSSplitViewItem.CollapseBehavior.preferResizingSiblingsWithFixedSplitView](nssplitviewitem/collapsebehavior-swift.enum/preferresizingsiblingswithfixedsplitview.md)
  The item’s preference is to resize the other split panes.
- [NSSplitViewItem.CollapseBehavior.useConstraints](nssplitviewitem/collapsebehavior-swift.enum/useconstraints.md)
  The item collapses and expands using a constraint animation, with a constraint priority of the item’s holding priority.
### Initializers
- [init?(rawValue: Int)](nssplitviewitem/collapsebehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isCollapsed: Bool](nssplitviewitem/iscollapsed.md)
  A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.
- [var canCollapse: Bool](nssplitviewitem/cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [var isSpringLoaded: Bool](nssplitviewitem/isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.
- [var canCollapseFromWindowResize: Bool](nssplitviewitem/cancollapsefromwindowresize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.enum)*
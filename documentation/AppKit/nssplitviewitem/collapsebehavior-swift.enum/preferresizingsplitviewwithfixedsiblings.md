# NSSplitViewItem.CollapseBehavior.preferResizingSplitViewWithFixedSiblings

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The item’s preference is to keep the other panes at their current size and position onscreen, potentially growing or shrinking the window in the direction to best preserve that.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case preferResizingSplitViewWithFixedSiblings
```

```c
NSSplitViewItemCollapseBehaviorPreferResizingSplitViewWithFixedSiblings
```

#### Discussion

The split view item breaks this preference in full-screen mode, and to keep the window fully onscreen during resizing.

## See Also

### Constants
- [NSSplitViewItem.CollapseBehavior.default](./default.md)
  The item uses the default collapsing behavior.
- [NSSplitViewItem.CollapseBehavior.preferResizingSiblingsWithFixedSplitView](./preferresizingsiblingswithfixedsplitview.md)
  The item’s preference is to resize the other split panes.
- [NSSplitViewItem.CollapseBehavior.useConstraints](./useconstraints.md)
  The item collapses and expands using a constraint animation, with a constraint priority of the item’s holding priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.enum/preferresizingsplitviewwithfixedsiblings)*
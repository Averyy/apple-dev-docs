# NSSplitViewItem.CollapseBehavior.preferResizingSiblingsWithFixedSplitView

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The item’s preference is to resize the other split panes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case preferResizingSiblingsWithFixedSplitView
```

```c
NSSplitViewItemCollapseBehaviorPreferResizingSiblingsWithFixedSplitView
```

## Discussion

The split view item breaks this preference if it can’t fully expand without causing the other split panes to resize below their minimum size threshold.

## See Also

### Constants
- [NSSplitViewItem.CollapseBehavior.default](./default.md)
  The item uses the default collapsing behavior.
- [NSSplitViewItem.CollapseBehavior.preferResizingSplitViewWithFixedSiblings](./preferresizingsplitviewwithfixedsiblings.md)
  The item’s preference is to keep the other panes at their current size and position onscreen, potentially growing or shrinking the window in the direction to best preserve that.
- [NSSplitViewItem.CollapseBehavior.useConstraints](./useconstraints.md)
  The item collapses and expands using a constraint animation, with a constraint priority of the item’s holding priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.enum/preferresizingsiblingswithfixedsplitview)*
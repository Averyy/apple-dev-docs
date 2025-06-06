# NSSplitViewItem.CollapseBehavior.preferResizingSiblingsWithFixedSplitView

**Framework**: AppKit  
**Kind**: case

The item’s preference is to resize the other split panes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case preferResizingSiblingsWithFixedSplitView
```

#### Discussion

The split view item breaks this preference if it can’t fully expand without causing the other split panes to resize below their minimum size threshold.

## See Also

- [NSSplitViewItem.CollapseBehavior.default](nssplitviewitem/collapsebehavior-swift.enum/default.md)
  The item uses the default collapsing behavior.
- [NSSplitViewItem.CollapseBehavior.preferResizingSplitViewWithFixedSiblings](nssplitviewitem/collapsebehavior-swift.enum/preferresizingsplitviewwithfixedsiblings.md)
  The item’s preference is to keep the other panes at their current size and position onscreen, potentially growing or shrinking the window in the direction to best preserve that.
- [NSSplitViewItem.CollapseBehavior.useConstraints](nssplitviewitem/collapsebehavior-swift.enum/useconstraints.md)
  The item collapses and expands using a constraint animation, with a constraint priority of the item’s holding priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.enum/preferresizingsiblingswithfixedsplitview)*
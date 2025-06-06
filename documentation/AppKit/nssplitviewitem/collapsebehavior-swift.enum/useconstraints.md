# NSSplitViewItem.CollapseBehavior.useConstraints

**Framework**: AppKit  
**Kind**: case

The item collapses and expands using a constraint animation, with a constraint priority of the item’s holding priority.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case useConstraints
```

#### Discussion

This collapse behavior may result in a partial internal content resize and window resize, and doesn’t affect whether the window stays onscreen. You can use external constraints to adjust how the animation affects the item, its sibling items, and the window’s size and position.

## See Also

- [NSSplitViewItem.CollapseBehavior.default](nssplitviewitem/collapsebehavior-swift.enum/default.md)
  The item uses the default collapsing behavior.
- [NSSplitViewItem.CollapseBehavior.preferResizingSplitViewWithFixedSiblings](nssplitviewitem/collapsebehavior-swift.enum/preferresizingsplitviewwithfixedsiblings.md)
  The item’s preference is to keep the other panes at their current size and position onscreen, potentially growing or shrinking the window in the direction to best preserve that.
- [NSSplitViewItem.CollapseBehavior.preferResizingSiblingsWithFixedSplitView](nssplitviewitem/collapsebehavior-swift.enum/preferresizingsiblingswithfixedsplitview.md)
  The item’s preference is to resize the other split panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.enum/useconstraints)*
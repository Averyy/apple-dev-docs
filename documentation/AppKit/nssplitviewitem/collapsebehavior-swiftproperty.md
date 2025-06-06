# collapseBehavior

**Framework**: AppKit  
**Kind**: property

The resizing behavior when the split view item toggles its collapsed state.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var collapseBehavior: NSSplitViewItem.CollapseBehavior { get set }
```

#### Discussion

The default value of this property is [`NSSplitViewItem.CollapseBehavior.default`](nssplitviewitem/collapsebehavior-swift.enum/default.md).

## See Also

- [var isCollapsed: Bool](nssplitviewitem/iscollapsed.md)
  A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.
- [var canCollapse: Bool](nssplitviewitem/cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.enum.md)
  Constants that describe the split view item’s collapsing behavior.
- [var isSpringLoaded: Bool](nssplitviewitem/isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.
- [var canCollapseFromWindowResize: Bool](nssplitviewitem/cancollapsefromwindowresize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior-swift.property)*
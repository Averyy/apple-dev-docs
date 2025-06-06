# isCollapsed

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isCollapsed: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var canCollapse: Bool](nssplitviewitem/cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.enum.md)
  Constants that describe the split view item’s collapsing behavior.
- [var isSpringLoaded: Bool](nssplitviewitem/isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.
- [var canCollapseFromWindowResize: Bool](nssplitviewitem/cancollapsefromwindowresize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/iscollapsed)*
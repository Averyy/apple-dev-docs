# isSpringLoaded

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the split view item can temporarily expand during a drag.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var isSpringLoaded: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the split view item can temporarily expand during a drag if the user hovers or force clicks its neighboring divider.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isCollapsed: Bool](nssplitviewitem/iscollapsed.md)
  A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.
- [var canCollapse: Bool](nssplitviewitem/cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.enum.md)
  Constants that describe the split view item’s collapsing behavior.
- [var canCollapseFromWindowResize: Bool](nssplitviewitem/cancollapsefromwindowresize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/isspringloaded)*
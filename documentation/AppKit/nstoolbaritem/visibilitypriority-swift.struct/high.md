# high

**Framework**: AppKit  
**Kind**: property

A high priority that makes it less likely for the toolbar item to move to the overflow item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
static let high: NSToolbarItem.VisibilityPriority
```

#### Discussion

The toolbar moves items with [`standard`](nstoolbaritem/visibilitypriority-swift.struct/standard.md) priority to the overflow menu before it moves items with this priority.

## See Also

- [static let standard: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/standard.md)
  The default visibility priority.
- [static let low: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/low.md)
  The lowest-priority for a toolbar item.
- [static let user: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/user.md)
  The highest priority for items in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct/high)*
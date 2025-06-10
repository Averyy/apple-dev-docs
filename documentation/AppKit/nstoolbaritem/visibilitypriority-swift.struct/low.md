# low

**Framework**: AppKit  
**Kind**: property

The lowest-priority for a toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
static let low: NSToolbarItem.VisibilityPriority
```

#### Discussion

The toolbar pushes items with this priority to the overflow menu first, even before items with the [`standard`](nstoolbaritem/visibilitypriority-swift.struct/standard.md) priority.

## See Also

- [static let standard: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/standard.md)
  The default visibility priority.
- [static let high: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/high.md)
  A high priority that makes it less likely for the toolbar item to move to the overflow item.
- [static let user: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/user.md)
  The highest priority for items in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct/low)*
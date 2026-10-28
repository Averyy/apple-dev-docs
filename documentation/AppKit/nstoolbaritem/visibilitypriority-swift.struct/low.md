# low

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The lowest-priority for a toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
static var low: NSToolbarItem.VisibilityPriority { get }
```

```c
static const NSToolbarItemVisibilityPriority NSToolbarItemVisibilityPriorityLow;
```

## Discussion

The toolbar pushes items with this priority to the overflow menu first, even before items with the [`standard`](./standard.md) priority.

## See Also

### Visibility priorities
- [static var standard: NSToolbarItem.VisibilityPriority](./standard.md)
  The default visibility priority.
- [static var high: NSToolbarItem.VisibilityPriority](./high.md)
  A high priority that makes it less likely for the toolbar item to move to the overflow item.
- [static var user: NSToolbarItem.VisibilityPriority](./user.md)
  The highest priority for items in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct/low)*
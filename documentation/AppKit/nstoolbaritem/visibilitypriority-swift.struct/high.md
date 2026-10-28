# high

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A high priority that makes it less likely for the toolbar item to move to the overflow item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
static var high: NSToolbarItem.VisibilityPriority { get }
```

```c
static const NSToolbarItemVisibilityPriority NSToolbarItemVisibilityPriorityHigh;
```

## Discussion

The toolbar moves items with [`standard`](./standard.md) priority to the overflow menu before it moves items with this priority.

## See Also

### Visibility priorities
- [static var standard: NSToolbarItem.VisibilityPriority](./standard.md)
  The default visibility priority.
- [static var low: NSToolbarItem.VisibilityPriority](./low.md)
  The lowest-priority for a toolbar item.
- [static var user: NSToolbarItem.VisibilityPriority](./user.md)
  The highest priority for items in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct/high)*
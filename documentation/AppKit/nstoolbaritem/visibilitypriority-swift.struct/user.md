# user

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The highest priority for items in the toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
static var user: NSToolbarItem.VisibilityPriority { get }
```

```c
static const NSToolbarItemVisibilityPriority NSToolbarItemVisibilityPriorityUser;
```

#### Discussion

The toolbar pushes these items to the overflow menu last.

## See Also

### Visibility priorities
- [static var standard: NSToolbarItem.VisibilityPriority](./standard.md)
  The default visibility priority.
- [static var low: NSToolbarItem.VisibilityPriority](./low.md)
  The lowest-priority for a toolbar item.
- [static var high: NSToolbarItem.VisibilityPriority](./high.md)
  A high priority that makes it less likely for the toolbar item to move to the overflow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct/user)*
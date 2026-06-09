# low

**Framework**: SwiftUI  
**Kind**: property

A priority that moves the item to the overflow menu before items with the default or high priority.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.1+

## Declaration

```swift
static let low: ToolbarItemVisibilityPriority
```

#### Discussion

Use for secondary actions, such as archive or delete, that don’t need persistent visibility in the toolbar.

## See Also

- [static let automatic: ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority/automatic.md)
  The default priority that lets the system determine the item’s visibility in the toolbar.
- [static let high: ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority/high.md)
  A priority that keeps the item in the toolbar longer than items with the default or low priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/low)*
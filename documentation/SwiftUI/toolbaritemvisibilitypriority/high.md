# high

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A priority that keeps the item in the toolbar longer than items with the default or low priority.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 26.1+

## Declaration

```swift
static let high: ToolbarItemVisibilityPriority
```

## Discussion

Use for frequently used actions that need to stay visible as the toolbar shrinks.

## See Also

### Getting system priorities
- [static let automatic: ToolbarItemVisibilityPriority](./automatic.md)
  The default priority that lets the system determine the item’s visibility in the toolbar.
- [static let low: ToolbarItemVisibilityPriority](./low.md)
  A priority that moves the item to the overflow menu before items with the default or high priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/high)*
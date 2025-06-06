# automatic

**Framework**: SwiftUI  
**Kind**: property

The system places the item automatically, depending on many factors including the platform, size class, or presence of other items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let automatic: ToolbarItemPlacement
```

#### Discussion

In macOS and in Mac Catalyst apps, the system places items in the current toolbar section in order of leading to trailing. On watchOS, only the first item appears, pinned beneath the navigation bar.

In iPadOS, the system places items in the center of the navigation bar if the navigation bar supports customization. Otherwise, it places items in the trailing position of the navigation bar.

In iOS, and tvOS, the system places items in the trailing position of the navigation bar.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar when determining how many items to render in the toolbar. If not all items fit in the available space, an overflow menu may be created and remaining items placed in that menu.

## See Also

- [static let principal: ToolbarItemPlacement](toolbaritemplacement/principal.md)
  The system places the item in the principal item section.
- [static let status: ToolbarItemPlacement](toolbaritemplacement/status.md)
  The item represents a change in status for the current context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/automatic)*
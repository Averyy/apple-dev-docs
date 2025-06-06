# status

**Framework**: SwiftUI  
**Kind**: property

The item represents a change in status for the current context.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
static let status: ToolbarItemPlacement
```

#### Discussion

Status items are informational in nature, and don’t represent an action that can be taken by the user. For example, a message that indicates the time of the last communication with the server to check for new messages.

In macOS and in Mac Catalyst apps, the system places status items in the center of the toolbar.

In iOS and iPadOS, the system places status items in the center of the bottom toolbar.

In tvOS, this placement is only available from within the sidebar of a [`NavigationSplitView`](navigationsplitview.md).  The system places status items in the center of the bottom toolbar within the navigation sidebar.  It has no effect if used elsewhere.

## See Also

- [static let automatic: ToolbarItemPlacement](toolbaritemplacement/automatic.md)
  The system places the item automatically, depending on many factors including the platform, size class, or presence of other items.
- [static let principal: ToolbarItemPlacement](toolbaritemplacement/principal.md)
  The system places the item in the principal item section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/status)*
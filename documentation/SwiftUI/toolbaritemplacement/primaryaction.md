# primaryAction

**Framework**: SwiftUI  
**Kind**: property

The item represents a primary action.

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
static let primaryAction: ToolbarItemPlacement
```

#### Discussion

A primary action is a more frequently used action for the current context. For example, a button the user clicks or taps to compose a new message in a chat app.

In macOS and in Mac Catalyst apps, the location for the primary action is the leading edge of the toolbar.

In iOS, iPadOS, and tvOS, the location for the primary action is the trailing edge of the navigation bar.

In watchOS the system places the primary action beneath the navigation bar; the user reveals the action by scrolling.

## See Also

- [static let secondaryAction: ToolbarItemPlacement](toolbaritemplacement/secondaryaction.md)
  The item represents a secondary action.
- [static let confirmationAction: ToolbarItemPlacement](toolbaritemplacement/confirmationaction.md)
  The item represents a confirmation action for a modal interface.
- [static let cancellationAction: ToolbarItemPlacement](toolbaritemplacement/cancellationaction.md)
  The item represents a cancellation action for a modal interface.
- [static let destructiveAction: ToolbarItemPlacement](toolbaritemplacement/destructiveaction.md)
  The item represents a destructive action for a modal interface.
- [static let navigation: ToolbarItemPlacement](toolbaritemplacement/navigation.md)
  The item represents a navigation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction)*
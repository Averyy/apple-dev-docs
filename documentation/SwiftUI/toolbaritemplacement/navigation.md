# navigation

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A placement for navigation actions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let navigation: ToolbarItemPlacement
```

## Discussion

Navigation actions allow the user to move between contexts. For example, the forward and back buttons of a web browser are navigation actions.

In macOS and in Mac Catalyst apps, the system places navigation items in the leading edge of the toolbar ahead of the inline title if that is present in the toolbar.

In iOS, iPadOS, and tvOS, navigation items appear in the leading edge of the navigation bar. If a system navigation item such as a back button is present in a compact width, it instead appears in the [`primaryAction`](./primaryaction.md) placement.

## See Also

### Getting placement for specific actions
- [static let primaryAction: ToolbarItemPlacement](./primaryaction.md)
  A placement for the primary action.
- [static let secondaryAction: ToolbarItemPlacement](./secondaryaction.md)
  A placement for secondary actions.
- [static let confirmationAction: ToolbarItemPlacement](./confirmationaction.md)
  A placement for confirmation actions in a modal interface.
- [static let cancellationAction: ToolbarItemPlacement](./cancellationaction.md)
  A placement for cancellation actions in a modal interface.
- [static let destructiveAction: ToolbarItemPlacement](./destructiveaction.md)
  A placement for destructive actions in a modal interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/navigation)*
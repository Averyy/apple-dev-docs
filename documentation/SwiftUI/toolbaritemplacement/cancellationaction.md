# cancellationAction

**Framework**: SwiftUI  
**Kind**: property

A placement for cancellation actions in a modal interface.

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
static let cancellationAction: ToolbarItemPlacement
```

#### Discussion

Cancellation actions dismiss the modal interface without taking any action, usually by tapping or clicking a Cancel button.

In macOS and in Mac Catalyst apps, the system places `cancellationAction` items on the trailing edge of the sheet but places them before any [`confirmationAction`](toolbaritemplacement/confirmationaction.md) items.

In iOS, iPadOS, tvOS, and watchOS, the system places `cancellationAction` items on the leading edge of the navigation bar.

## See Also

- [static let primaryAction: ToolbarItemPlacement](toolbaritemplacement/primaryaction.md)
  A placement for the primary action.
- [static let secondaryAction: ToolbarItemPlacement](toolbaritemplacement/secondaryaction.md)
  A placement for secondary actions.
- [static let confirmationAction: ToolbarItemPlacement](toolbaritemplacement/confirmationaction.md)
  A placement for confirmation actions in a modal interface.
- [static let destructiveAction: ToolbarItemPlacement](toolbaritemplacement/destructiveaction.md)
  A placement for destructive actions in a modal interface.
- [static let navigation: ToolbarItemPlacement](toolbaritemplacement/navigation.md)
  A placement for navigation actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/cancellationaction)*
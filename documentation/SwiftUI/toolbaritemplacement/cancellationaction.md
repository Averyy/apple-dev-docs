# cancellationAction

**Framework**: SwiftUI  
**Kind**: property

The item represents a cancellation action for a modal interface.

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
  The item represents a primary action.
- [static let secondaryAction: ToolbarItemPlacement](toolbaritemplacement/secondaryaction.md)
  The item represents a secondary action.
- [static let confirmationAction: ToolbarItemPlacement](toolbaritemplacement/confirmationaction.md)
  The item represents a confirmation action for a modal interface.
- [static let destructiveAction: ToolbarItemPlacement](toolbaritemplacement/destructiveaction.md)
  The item represents a destructive action for a modal interface.
- [static let navigation: ToolbarItemPlacement](toolbaritemplacement/navigation.md)
  The item represents a navigation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/cancellationaction)*
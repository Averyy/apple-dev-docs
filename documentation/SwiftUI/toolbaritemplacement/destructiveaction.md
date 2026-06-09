# destructiveAction

**Framework**: SwiftUI  
**Kind**: property

A placement for destructive actions in a modal interface.

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
static let destructiveAction: ToolbarItemPlacement
```

#### Discussion

Destructive actions represent the opposite of a confirmation action. For example, a button labeled “Don’t Save” that allows the user to discard unsaved changes to a document before quitting.

In macOS and in Mac Catalyst apps, the system places `destructiveAction` items in the leading edge of the sheet and gives them a special appearance to caution against accidental use.

In iOS, tvOS, and watchOS, the system places `destructiveAction` items in the trailing edge of the navigation bar.

## See Also

- [static let primaryAction: ToolbarItemPlacement](toolbaritemplacement/primaryaction.md)
  A placement for the primary action.
- [static let secondaryAction: ToolbarItemPlacement](toolbaritemplacement/secondaryaction.md)
  A placement for secondary actions.
- [static let confirmationAction: ToolbarItemPlacement](toolbaritemplacement/confirmationaction.md)
  A placement for confirmation actions in a modal interface.
- [static let cancellationAction: ToolbarItemPlacement](toolbaritemplacement/cancellationaction.md)
  A placement for cancellation actions in a modal interface.
- [static let navigation: ToolbarItemPlacement](toolbaritemplacement/navigation.md)
  A placement for navigation actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/destructiveaction)*
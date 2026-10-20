# confirmationAction

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A placement for confirmation actions in a modal interface.

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
static let confirmationAction: ToolbarItemPlacement
```

#### Discussion

Use confirmation actions to receive user confirmation of a particular action. An example of a confirmation action would be an action with the label “Add” to add a new event to the calendar.

In macOS and in Mac Catalyst apps, the system places `confirmationAction` items on the trailing edge in the trailing-most position of the sheet and gain the apps accent color as a background color.

In iOS, iPadOS, and tvOS, the system places `confirmationAction` items in the same location as a [`primaryAction`](./primaryaction.md) placement.

In watchOS, the system places `confirmationAction` items in the trailing edge of the navigation bar.

## See Also

### Getting placement for specific actions
- [static let primaryAction: ToolbarItemPlacement](./primaryaction.md)
  A placement for the primary action.
- [static let secondaryAction: ToolbarItemPlacement](./secondaryaction.md)
  A placement for secondary actions.
- [static let cancellationAction: ToolbarItemPlacement](./cancellationaction.md)
  A placement for cancellation actions in a modal interface.
- [static let destructiveAction: ToolbarItemPlacement](./destructiveaction.md)
  A placement for destructive actions in a modal interface.
- [static let navigation: ToolbarItemPlacement](./navigation.md)
  A placement for navigation actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/confirmationaction)*
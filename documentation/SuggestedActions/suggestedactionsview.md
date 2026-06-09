# SuggestedActionsView

**Framework**: Suggested Actions  
**Kind**: struct

A view that displays suggested actions for a message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
struct SuggestedActionsView
```

#### Overview

The suggested actions view displays inline actions for a messaging app, next to a message, using context you provide. This view animates suggested actions as they become available. If no suggested actions are available, the view’s size is zero and remains zero until they become available. At size zero, a `SuggestedActionsView` doesn’t affect your surrounding layout. As a result, place the view for every message in a conversation. It doesn’t introduce gaps between messages if a message doesn’t have suggested actions.

> **Note**: To display suggested actions, add the [`Suggested Actions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.suggested-actions) entitlement to your app target.

#### Customize the Appearance

To customize a `SuggestedActionsView`, apply standard SwiftUI view modifiers to change its appearance. Additionally, the view reads the following modifiers from its parent views:

- [`tint(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tint(_:)),
- [`foregroundStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/foregroundStyle(_:)),
- [`font(_:)`](https://developer.apple.com/documentation/SwiftUI/View/font(_:))
- [`buttonBorderShape(_:)`](https://developer.apple.com/documentation/SwiftUI/View/buttonBorderShape(_:))

#### Generate Suggested Actions for Future Use

To avoid showing a loading state when the view appears, call [`generate(message:previousMessages:)`](suggestedactionsview/generate(message:previousmessages:).md) to let the Suggested Actions framework create suggested actions and cache them for future use. When you later initialize a `SuggestedActionsView`, the framework checks the `id` of cached suggested actions based on their messages’ `id` property. If it finds an `id` that matches the `id` of a new [`SuggestedActionsMessage`](suggestedactionsmessage.md), the system uses the already generated suggested action.

The following example shows how an app might show a `SuggestedActionsView` with information about previous messages using a capsule border shape, blue tint, and the callout font style:

```swift
SuggestedActionsView(
    message: message.suggestedActionsMessage,
    previousMessages: message.previousMessages
        .suffix(SuggestedActionsMessage.previousMessagesLimit)
        .map(\.suggestedActionsMessage)
)
.buttonBorderShape(.capsule)
.tint(.blue)
.font(.callout)
```

## Topics

### Displaying suggested actions
- [init(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage])](suggestedactionsview/init(message:previousmessages:).md)
  Creates a view that shows suggested actions for the specified message.
- [static func generate(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage]) async](suggestedactionsview/generate(message:previousmessages:).md)
  Fetches and caches suggested actions for the provided message.
- [struct SuggestedActionsMessage](suggestedactionsmessage.md)
  A representation of the message you use as context for suggested actions.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsview)*
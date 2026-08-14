# Suggested Actions

**Framework**: Suggested Actions  
**Kind**: module

Offer quick actions next to messages in your messaging app, based on context you provide.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

#### Overview

When people send each other messages in your messaging app, they share information like dates, reminders, or other actionable content. To let people complete a message-related task in your messaging app with Suggested Actions, add a [`SuggestedActionsView`](suggestedactionsview.md) below a message and provide the view with message content. To preserve user privacy, the framework analyzes the message content you provide on-device and doesn’t send it to Apple servers.

By default, the `SuggestedActionsView` doesn’t take up space or affect your layout. When you provide it with message content, Suggested Actions identifies the suggested actions that apply to the message, then shows the [`SuggestedActionsView`](suggestedactionsview.md) inline, filled with actions a person can take. For example, Suggested Actions can detect and suggest actions such as:

- Creating an event in Calendar from a proposed meeting time
- Adding an entry in Reminders
- Opening a location in Maps

> **Note**: To use the Suggested Actions framework, add the [`Suggested Actions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.suggested-actions) entitlement to your app target.

## Topics

### Essentials
- [Suggested Actions](../bundleresources/entitlements/com.apple.developer.suggested-actions.md)
  A Boolean value that indicates whether a messaging app displays suggested actions for a message.
### Suggested actions for messages
- [struct SuggestedActionsView](suggestedactionsview.md)
  A view that displays suggested actions for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SuggestedActions)*
# SuggestedActionsMessage

**Framework**: Suggested Actions  
**Kind**: struct  
**Role**: Structure

A representation of the message you use as context for suggested actions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SuggestedActionsMessage
```

## Overview

Create a `SuggestedActionsMessage` from your app’s data model for a message, then pass it to [`init(message:previousMessages:)`](./suggestedactionsview/init%28message,previousmessages%29.md) or [`generate(message:previousMessages:)`](./suggestedactionsview/generate%28message,previousmessages%29.md).

The `id` you pass to the create a `SuggestedActionsMessage` must be unique for each message and stable across app launches. Creating stable identifiers lets the framework match messages against previously cached suggested actions.

> **Note**: To use the Suggested Actions framework, add the [`Suggested Actions`](../BundleResources/entitlements/com.apple.developer.suggested-actions.md) entitlement to your app target.

## Topics

### Creating the message representation
- [init(id: some Hashable, date: Date, subject: AttributedString?, body: AttributedString, sender: SuggestedActionsMessage.Participant, recipients: [SuggestedActionsMessage.Participant])](./suggestedactionsmessage/init%28id,date,subject,body,sender,recipients%29.md)
  Creates a representation of a message that the system uses to display suggested actions.
- [SuggestedActionsMessage.Participant](./suggestedactionsmessage/participant.md)
  A sender or recipient of a message in a conversation.
### Accessing the considered number of messages
- [static var previousMessagesLimit: Int](./suggestedactionsmessage/previousmessageslimit.md)
  The maximum number of previous messages that contribute to generating suggested actions.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Displaying suggested actions
- [init(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage])](./suggestedactionsview/init%28message,previousmessages%29.md)
  Creates a view that shows suggested actions for the specified message.
- [static func generate(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage]) async](./suggestedactionsview/generate%28message,previousmessages%29.md)
  Fetches and caches suggested actions for the provided message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage)*
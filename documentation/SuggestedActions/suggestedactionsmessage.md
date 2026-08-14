# SuggestedActionsMessage

**Framework**: Suggested Actions  
**Kind**: struct

A representation of the message you use as context for suggested actions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SuggestedActionsMessage
```

#### Overview

Create a `SuggestedActionsMessage` from your app’s data model for a message, then pass it to [`init(message:previousMessages:)`](suggestedactionsview/init(message:previousmessages:).md) or [`generate(message:previousMessages:)`](suggestedactionsview/generate(message:previousmessages:).md).

The `id` you pass to the create a `SuggestedActionsMessage` must be unique for each message and stable across app launches. Creating stable identifiers lets the framework match messages against previously cached suggested actions.

> **Note**: To use the Suggested Actions framework, add the [`Suggested Actions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.suggested-actions) entitlement to your app target.

## Topics

### Creating the message representation
- [init(id: some Hashable, date: Date, subject: AttributedString?, body: AttributedString, sender: SuggestedActionsMessage.Participant, recipients: [SuggestedActionsMessage.Participant])](suggestedactionsmessage/init(id:date:subject:body:sender:recipients:).md)
  Creates a representation of a message that the system uses to display suggested actions.
- [SuggestedActionsMessage.Participant](suggestedactionsmessage/participant.md)
  A sender or recipient of a message in a conversation.
### Accessing the considered number of messages
- [static var previousMessagesLimit: Int](suggestedactionsmessage/previousmessageslimit.md)
  The maximum number of previous messages that contribute to generating suggested actions.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage])](suggestedactionsview/init(message:previousmessages:).md)
  Creates a view that shows suggested actions for the specified message.
- [static func generate(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage]) async](suggestedactionsview/generate(message:previousmessages:).md)
  Fetches and caches suggested actions for the provided message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage)*
# init(id:date:subject:body:sender:recipients:)

**Framework**: Suggested Actions  
**Kind**: init

Creates a representation of a message that the system uses to display suggested actions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(id: some Hashable, date: Date, subject: AttributedString?, body: AttributedString, sender: SuggestedActionsMessage.Participant, recipients: [SuggestedActionsMessage.Participant])
```

## Parameters

- `id`: A stable, unique identifier for the message. Common types for this identifier are `String`, `UUID`, or a custom identifier type, but any `Hashable` value works. The identifier must remain consistent across the lifetime of the message and across app launches.
- `date`: The date when the sender sent the message or the date your app received it.
- `subject`: The subject line of the message.
- `body`: The body content of the message.
- `sender`: The participant who sent the message.
- `recipients`: The participants who received the message.

## See Also

- [SuggestedActionsMessage.Participant](suggestedactionsmessage/participant.md)
  A sender or recipient of a message in a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage/init(id:date:subject:body:sender:recipients:))*
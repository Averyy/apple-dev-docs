# AssistantSchemas.MailEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe email.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol MailEntity : AssistantSchemas.Model
```

## Mentions

- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var account: some AssistantSchemas.Entity](assistantschemas/mailentity/account.md)
  The app entity describes an email account.
- [var draft: some AssistantSchemas.Entity](assistantschemas/mailentity/draft.md)
  The app entity describes an email draft.
- [var mailbox: some AssistantSchemas.Entity](assistantschemas/mailentity/mailbox.md)
  The app entity describes an email mailbox.
- [var message: some AssistantSchemas.Entity](assistantschemas/mailentity/message.md)
  The app entity describes an email message.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s email functionality with Siri and Apple Intelligence.
- [AssistantSchemas.MailIntent](assistantschemas/mailintent.md)
  Assistant schema conformance for app intents that offer email functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailentity)*
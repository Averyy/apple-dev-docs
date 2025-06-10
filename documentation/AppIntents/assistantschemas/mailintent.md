# AssistantSchemas.MailIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer email functionality.

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
protocol MailIntent : AssistantSchemas.Model
```

## Mentions

- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var archiveMail: some AssistantSchemas.Intent](assistantschemas/mailintent/archivemail.md)
  The app intent conforms to the schema for archiving an email message.
- [var createDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/createdraft.md)
  The app intent conforms to the schema for creating an email draft.
- [var deleteDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/deletedraft.md)
  The app intent conforms to the schema for deleting an email draft.
- [var deleteMail: some AssistantSchemas.Intent](assistantschemas/mailintent/deletemail.md)
  The app intent conforms to the schema for deleting email messages.
- [var forwardMail: some AssistantSchemas.Intent](assistantschemas/mailintent/forwardmail.md)
  The app intent conforms to the schema for forwarding an email message.
- [var replyMail: some AssistantSchemas.Intent](assistantschemas/mailintent/replymail.md)
  The app intent conforms to the schema for replying to an email message.
- [var saveDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/savedraft.md)
  The app intent conforms to the schema for saving an email draft.
- [var sendDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/senddraft.md)
  The app intent conforms to the schema for sending an email draft.
- [var updateDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/updatedraft.md)
  The app intent conforms to the schema for updating an email draft.
- [var updateMail: some AssistantSchemas.Intent](assistantschemas/mailintent/updatemail.md)
  The app intent conforms to the schema for updating email messages.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s email functionality with Siri and Apple Intelligence.
- [AssistantSchemas.MailEntity](assistantschemas/mailentity.md)
  Assistant schema conformance for app entities that describe email.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailintent)*
# AppSchema.MailIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the mail domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol MailIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var archiveMail: some AppSchemaIntent](./mailintent/archivemail.md)
  An intent schema that archives one or more email messages.
- [var createDraft: some AppSchemaIntent](./mailintent/createdraft.md)
  An intent schema that opens an email composer to draft an email.
- [var deleteDraft: some AppSchemaIntent](./mailintent/deletedraft.md)
  An intent schema that deletes one or more email drafts.
- [var deleteMail: some AppSchemaIntent](./mailintent/deletemail.md)
  An intent schema that deletes one or more email messages.
- [var forwardMail: some AppSchemaIntent](./mailintent/forwardmail.md)
  An intent schema that opens an email composer to forward an email.
- [var openDraft: some AppSchemaIntent](./mailintent/opendraft.md)
  An intent schema that opens an email draft.
- [var openMessage: some AppSchemaIntent](./mailintent/openmessage.md)
  An intent schema that opens an email message.
- [var replyMail: some AppSchemaIntent](./mailintent/replymail.md)
  An intent schema that opens an email composer to reply to an email.
- [var saveDraft: some AppSchemaIntent](./mailintent/savedraft.md)
  An intent schema that saves an email draft.
- [var sendDraft: some AppSchemaIntent](./mailintent/senddraft.md)
  An intent schema that sends an email draft or schedules it to be sent later.
- [var updateDraft: some AppSchemaIntent](./mailintent/updatedraft.md)
  An intent schema that makes updates to an email draft.
- [var updateMail: some AppSchemaIntent](./mailintent/updatemail.md)
  An intent schema that makes updates to one or more existing email messages by modifying the status, flags, and location.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var archiveMail: some AppSchemaIntent](./mailintent/archivemail.md)
  An intent schema that archives one or more email messages.
- [var createDraft: some AppSchemaIntent](./mailintent/createdraft.md)
  An intent schema that opens an email composer to draft an email.
- [var deleteDraft: some AppSchemaIntent](./mailintent/deletedraft.md)
  An intent schema that deletes one or more email drafts.
- [var deleteMail: some AppSchemaIntent](./mailintent/deletemail.md)
  An intent schema that deletes one or more email messages.
- [var forwardMail: some AppSchemaIntent](./mailintent/forwardmail.md)
  An intent schema that opens an email composer to forward an email.
- [var openDraft: some AppSchemaIntent](./mailintent/opendraft.md)
  An intent schema that opens an email draft.
- [var openMessage: some AppSchemaIntent](./mailintent/openmessage.md)
  An intent schema that opens an email message.
- [var replyMail: some AppSchemaIntent](./mailintent/replymail.md)
  An intent schema that opens an email composer to reply to an email.
- [var saveDraft: some AppSchemaIntent](./mailintent/savedraft.md)
  An intent schema that saves an email draft.
- [var sendDraft: some AppSchemaIntent](./mailintent/senddraft.md)
  An intent schema that sends an email draft or schedules it to be sent later.
- [var updateDraft: some AppSchemaIntent](./mailintent/updatedraft.md)
  An intent schema that makes updates to an email draft.
- [var updateMail: some AppSchemaIntent](./mailintent/updatemail.md)
  An intent schema that makes updates to one or more existing email messages by modifying the status, flags, and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailintent)*
# openMessage

**Framework**: App Intents  
**Kind**: property

An intent schema that opens an email message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var openMessage: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `mail` domain and one of your app’s actions matches the `openMessage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .mail.openMessage)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `openMessage` schema:

```swift
@AppIntent(schema: .mail.openMessage)
struct MailOpenMessage: OpenIntent {
    var target: <#MailMessageEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var archiveMail: some AppSchemaIntent](appschema/mailintent/archivemail.md)
  An intent schema that archives one or more email messages.
- [var createDraft: some AppSchemaIntent](appschema/mailintent/createdraft.md)
  An intent schema that opens an email composer to draft an email.
- [var deleteDraft: some AppSchemaIntent](appschema/mailintent/deletedraft.md)
  An intent schema that deletes one or more email drafts.
- [var deleteMail: some AppSchemaIntent](appschema/mailintent/deletemail.md)
  An intent schema that deletes one or more email messages.
- [var forwardMail: some AppSchemaIntent](appschema/mailintent/forwardmail.md)
  An intent schema that opens an email composer to forward an email.
- [var openDraft: some AppSchemaIntent](appschema/mailintent/opendraft.md)
  An intent schema that opens an email draft.
- [var replyMail: some AppSchemaIntent](appschema/mailintent/replymail.md)
  An intent schema that opens an email composer to reply to an email.
- [var saveDraft: some AppSchemaIntent](appschema/mailintent/savedraft.md)
  An intent schema that saves an email draft.
- [var sendDraft: some AppSchemaIntent](appschema/mailintent/senddraft.md)
  An intent schema that sends an email draft or schedules it to be sent later.
- [var updateDraft: some AppSchemaIntent](appschema/mailintent/updatedraft.md)
  An intent schema that makes updates to an email draft.
- [var updateMail: some AppSchemaIntent](appschema/mailintent/updatemail.md)
  An intent schema that makes updates to one or more existing email messages by modifying the status, flags, and location.
- [AppSchema.MailIntent](appschema/mailintent.md)
  Identifies intent schemas in the mail domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailintent/openmessage)*
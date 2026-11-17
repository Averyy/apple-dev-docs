# createDraft

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens an email composer to draft an email.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var createDraft: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `mail` domain and one of your app’s actions matches the `createDraft` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .mail.createDraft)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createDraft` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `mail_createDraft` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .mail.createDraft)
struct CreateDraftIntent {
    /// Body text of the email message.
    var body: AttributedString?

    /// Recipients of the email message.
    var to: [IntentPerson]

    /// Subject of the email message.
    var subject: String?

    /// Cc recipients of the email message.
    var cc: [IntentPerson]

    /// Bcc recipients of the email message.
    var bcc: [IntentPerson]

    /// Account to send the email message with.
    var account: <#MailAccountEntity#>?

    /// Attachments of the email message.
    var attachments: [IntentFile]

    func perform() async throws -> some ReturnsValue<<#MailDraftEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create-draft intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `body` | `AttributedString?` | Foundation | Body text of the email message. |
| `to` | `[IntentPerson]` | App Intents | Recipients of the email message. |
| `subject` | `String?` | Swift | Subject of the email message. |
| `cc` | `[IntentPerson]` | App Intents | Cc recipients of the email message. |
| `bcc` | `[IntentPerson]` | App Intents | Bcc recipients of the email message. |
| `account` | `@AppEntity(schema: .mail.account)?` | Your app | Account to send the email message with. `MailAccountEntity` is a placeholder name for a type that conforms to the [`account`](../mailentity/account.md) entity schema, which your app defines and implements. |
| `attachments` | `[IntentFile]` | App Intents | Attachments of the email message. |

## See Also

### Actions
- [var archiveMail: some AppSchemaIntent](./archivemail.md)
  An intent schema that archives one or more email messages.
- [var deleteDraft: some AppSchemaIntent](./deletedraft.md)
  An intent schema that deletes one or more email drafts.
- [var deleteMail: some AppSchemaIntent](./deletemail.md)
  An intent schema that deletes one or more email messages.
- [var forwardMail: some AppSchemaIntent](./forwardmail.md)
  An intent schema that opens an email composer to forward an email.
- [var openDraft: some AppSchemaIntent](./opendraft.md)
  An intent schema that opens an email draft.
- [var openMessage: some AppSchemaIntent](./openmessage.md)
  An intent schema that opens an email message.
- [var replyMail: some AppSchemaIntent](./replymail.md)
  An intent schema that opens an email composer to reply to an email.
- [var saveDraft: some AppSchemaIntent](./savedraft.md)
  An intent schema that saves an email draft.
- [var sendDraft: some AppSchemaIntent](./senddraft.md)
  An intent schema that sends an email draft or schedules it to be sent later.
- [var updateDraft: some AppSchemaIntent](./updatedraft.md)
  An intent schema that makes updates to an email draft.
- [var updateMail: some AppSchemaIntent](./updatemail.md)
  An intent schema that makes updates to one or more existing email messages by modifying the status, flags, and location.
- [AppSchema.MailIntent](../mailintent.md)
  Identifies intent schemas in the mail domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailintent/createdraft)*
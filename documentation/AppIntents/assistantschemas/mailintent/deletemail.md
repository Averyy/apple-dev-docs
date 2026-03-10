# deleteMail

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for deleting email messages.

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
var deleteMail: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.mail.deleteMail` schema:

```swift
@AppIntent(schema: .mail.deleteMail)
struct DeleteMailIntent: DeleteIntent {
    @Parameter
    var entities: [MailMessageEntity]

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.mail` app intent domain, see [`Making email actions available to Siri and Apple Intelligence`](making-email-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var archiveMail: some AssistantSchemas.Intent](assistantschemas/mailintent/archivemail.md)
  The app intent conforms to the schema for archiving an email message.
- [var createDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/createdraft.md)
  The app intent conforms to the schema for creating an email draft.
- [var deleteDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/deletedraft.md)
  The app intent conforms to the schema for deleting an email draft.
- [var forwardMail: some AssistantSchemas.Intent](assistantschemas/mailintent/forwardmail.md)
  The app intent conforms to the schema for forwarding an email message.
- [var replyMail: some AssistantSchemas.Intent](assistantschemas/mailintent/replymail.md)
  The app intent conforms to the schema for replying to an email message.
- [var saveDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/savedraft.md)
  The app intent conforms to the schema for saving an email draft.
- [var updateDraft: some AssistantSchemas.Intent](assistantschemas/mailintent/updatedraft.md)
  The app intent conforms to the schema for updating an email draft.
- [var updateMail: some AssistantSchemas.Intent](assistantschemas/mailintent/updatemail.md)
  The app intent conforms to the schema for updating email messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailintent/deletemail)*
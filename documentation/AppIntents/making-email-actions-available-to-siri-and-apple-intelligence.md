# Making email actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s email functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s email capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app entity implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows someone to draft an email and send that at a later date and time, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.mail` domain and the [`sendDraft`](assistantschemas/mailintent/senddraft.md) schema:

```swift
@AppIntent(schema: .mail.sendDraft)
struct SendDraftIntent: AppIntent {
    var target: MailDraftEntity
    var sendLaterDate: Date?

    @MainActor
    func perform() async throws -> some IntentResult {
        return .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intent schemas in the `.mail` domain, see [`AssistantSchemas.MailIntent`](assistantschemas/mailintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `MailDraftEntity`. The following code snippet shows how the `MailDraftEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AppEntity(schema: .mail.draft)
struct MailDraftEntity {

    static var defaultQuery = Query()
    
    struct Query: EntityStringQuery {
        init() {}
        func entities(for identifiers: [MailDraftEntity.ID]) async throws -> [MailDraftEntity] { [] }
        func entities(matching string: String) async throws -> [MailDraftEntity] { [] }
    }

    var displayRepresentation: DisplayRepresentation { "Provide a display representation." }

    let id = UUID()

    var to: [IntentPerson]
    var cc: [IntentPerson]
    var bcc: [IntentPerson]
    var subject: String?
    var body: AttributedString?
    var attachments: [IntentFile]
    var account: MailAccountEntity
}
```

The assistant schema for the `MailDraftEntity` consists of the `.mail` domain and the [`draft`](assistantschemas/mailentity/draft.md) schema.

For a list of available app entity schemas in the `.mail` domain, see [`AssistantSchemas.MailEntity`](assistantschemas/mailentity.md).

## See Also

- [AssistantSchemas.MailIntent](assistantschemas/mailintent.md)
  Assistant schema conformance for app intents that offer email functionality.
- [AssistantSchemas.MailEntity](assistantschemas/mailentity.md)
  Assistant schema conformance for app entities that describe email.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-email-actions-available-to-siri-and-apple-intelligence)*
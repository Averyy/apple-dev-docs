# draft

**Framework**: App Intents  
**Kind**: property

The app entity describes an email draft.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var draft: some AssistantSchemas.Entity { get }
```

## Mentions

- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.mail` app intent domain, see [`Making email actions available to Siri and Apple Intelligence`](making-email-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.mail.draft` schema:

```swift
@AssistantEntity(schema: .mail.draft)
struct MailDraftEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [MailDraftEntity.ID]) async throws -> [MailDraftEntity] { [] }
        func entities(matching string: String) async throws -> [MailDraftEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Mail Draft" }

    let id = UUID()

    @Property
    var to: [IntentPerson]

    @Property
    var cc: [IntentPerson]

    @Property
    var bcc: [IntentPerson]

    @Property
    var subject: String?

    @Property
    var body: String?

    @Property
    var attachments: [IntentFile]

    @Property
    var account: MailAccountEntity
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailentity/draft)*
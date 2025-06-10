# message

**Framework**: App Intents  
**Kind**: property

The app entity describes an email message.

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
var message: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.mail.message` schema:

```swift
@AssistantEntity(schema: .mail.message)
struct MailMessageEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [MailMessageEntity.ID]) async throws -> [MailMessageEntity] { [] }
        func entities(matching string: String) async throws -> [MailMessageEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Mail Message" }

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
    var body: AttributedString?

    @Property
    var attachments: [IntentFile]

    @Property
    var sender: IntentPerson

    @Property
    var dateSent: Date

    @Property
    var dateReceived: Date

    @Property
    var isRead: Bool

    @Property
    var isJunk: Bool

    @Property
    var isFlagged: Bool

    @Property
    var account: MailAccountEntity

    @Property
    var mailbox: MailboxEntity
}
```

For more information about the `.mail` app intent domain, see [`Making email actions available to Siri and Apple Intelligence`](making-email-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entityschema/message)*
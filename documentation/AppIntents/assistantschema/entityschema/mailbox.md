# mailbox

**Framework**: App Intents  
**Kind**: property

The app entity describes an email mailbox.

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
var mailbox: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.mail` app intent domain, see [`Making email actions available to Siri and Apple Intelligence`](making-email-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.mail.mailbox` schema:

```swift
@AssistantEntity(schema: .mail.mailbox)
struct MailboxEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [MailboxEntity.ID]) async throws -> [MailboxEntity] { [] }
        func entities(matching string: String) async throws -> [MailboxEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Mailbox" }

    let id = UUID()

    @Property
    var name: String

    @Property
    var account: MailAccountEntity
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/entityschema/mailbox)*
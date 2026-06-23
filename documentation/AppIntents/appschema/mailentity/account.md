# account

**Framework**: App Intents  
**Kind**: property

An entity schema for an account.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var account: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `mail` domain and its content matches the `account` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .mail.account)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `account` schema:

```swift
@AppEntity(schema: .mail.account)
struct MailAccountEntity {
    // MARK: Static

    static let defaultQuery = MailAccountEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var emailAddress: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct MailAccountEntityQuery: EntityQuery {
        func entities(for identifiers: [MailAccountEntity.ID]) async throws -> [MailAccountEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var draft: some AppSchemaEntity](appschema/mailentity/draft.md)
  An entity schema for a draft.
- [var mailbox: some AppSchemaEntity](appschema/mailentity/mailbox.md)
  An entity schema for a mailbox.
- [var message: some AppSchemaEntity](appschema/mailentity/message.md)
  An entity schema for a message.
- [var thread: some AppSchemaEntity](appschema/mailentity/thread.md)
  An entity schema for a thread.
- [AppSchema.MailEntity](appschema/mailentity.md)
  Identifies entity schemas in the mail domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailentity/account)*
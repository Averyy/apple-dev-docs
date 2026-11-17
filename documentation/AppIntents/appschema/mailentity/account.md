# account

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an account.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var account: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `mail` domain and its content matches the `account` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .mail.account)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `account` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `mail_account` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .mail.account)
struct MailAccountEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more account entities, unless you provide another.
    static let defaultQuery = MailAccountEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the account entity.
    let id: <#Identifiable.ID#>

    var name: String

    var emailAddress: String

    /// The details the system shows to identify the account entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more account entities by their identifiers.
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

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the account entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |
| `emailAddress` | `String` | Swift | Email Address |

## See Also

### Content and parameter types
- [var draft: some AppSchemaEntity](./draft.md)
  An entity schema for a draft.
- [var mailbox: some AppSchemaEntity](./mailbox.md)
  An entity schema for a mailbox.
- [var message: some AppSchemaEntity](./message.md)
  An entity schema for a message.
- [var thread: some AppSchemaEntity](./thread.md)
  An entity schema for a thread.
- [AppSchema.MailEntity](../mailentity.md)
  Identifies entity schemas in the mail domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailentity/account)*
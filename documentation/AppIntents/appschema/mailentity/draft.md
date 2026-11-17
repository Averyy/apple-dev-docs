# draft

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a draft.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var draft: some AppSchemaEntity { get }
```

## Mentions

- [Making actions and content discoverable by Apple Intelligence](../../making-actions-and-content-discoverable-by-apple-intelligence.md)

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `mail` domain and its content matches the `draft` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .mail.draft)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `draft` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `mail_draft` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .mail.draft)
struct MailDraftEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more draft message entities, unless you provide another.
    static let defaultQuery = MailDraftEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the draft message entity.
    let id: <#Identifiable.ID#>

    var to: [IntentPerson]

    var cc: [IntentPerson]

    var bcc: [IntentPerson]

    var subject: String?

    var body: AttributedString?

    var attachments: [IntentFile]

    var account: <#MailAccountEntity#>

    /// The details the system shows to identify the draft message entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more draft message entities by their identifiers.
    struct MailDraftEntityQuery: EntityQuery {
        func entities(for identifiers: [MailDraftEntity.ID]) async throws -> [MailDraftEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the draft entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `to` | `[IntentPerson]` | App Intents | To |
| `cc` | `[IntentPerson]` | App Intents | Cc |
| `bcc` | `[IntentPerson]` | App Intents | Bcc |
| `subject` | `String?` | Swift | Subject |
| `body` | `AttributedString?` | Foundation | Body |
| `attachments` | `[IntentFile]` | App Intents | Attachments |
| `account` | `@AppEntity(schema: .mail.account)` | Your app | Account `MailAccountEntity` is a placeholder name for a type that conforms to the [`account`](./account.md) entity schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var account: some AppSchemaEntity](./account.md)
  An entity schema for an account.
- [var mailbox: some AppSchemaEntity](./mailbox.md)
  An entity schema for a mailbox.
- [var message: some AppSchemaEntity](./message.md)
  An entity schema for a message.
- [var thread: some AppSchemaEntity](./thread.md)
  An entity schema for a thread.
- [AppSchema.MailEntity](../mailentity.md)
  Identifies entity schemas in the mail domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailentity/draft)*
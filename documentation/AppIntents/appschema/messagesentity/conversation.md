# conversation

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a conversation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var conversation: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `messages` domain and its content matches the `conversation` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .messages.conversation)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `conversation` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `messages_conversation` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .messages.conversation)
struct ConversationEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more conversation entities, unless you provide another.
    static let defaultQuery = ConversationEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the conversation entity.
    let id: <#Identifiable.ID#>

    var recipients: [<#MessagePerson#>]

    var displayName: String

    var previewText: AttributedString

    var conversationName: String?

    var isRead: Bool

    var attributes: Set<<#ConversationAttribute#>>

    var dateLastActive: Date?

    /// The details the system shows to identify the conversation entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more conversation entities by their identifiers.
    struct ConversationEntityQuery: EntityQuery {
        func entities(for identifiers: [ConversationEntity.ID]) async throws -> [ConversationEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the conversation entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `recipients` | `[@AppEntity(schema: .messages.messagePerson)]` | Your app | Recipients `MessagePerson` is a placeholder name for a type that conforms to the [`messagePerson`](./messageperson.md) entity schema, which your app defines and implements. |
| `displayName` | `String` | Swift | Display Name |
| `previewText` | `AttributedString` | Foundation | Last Message |
| `conversationName` | `String?` | Swift | Group Name |
| `isRead` | `Bool` | Swift | Is Read |
| `attributes` | `Set<@AppEnum(schema: .messages.conversationAttribute)>` | Your app | Attributes `ConversationAttribute` is a placeholder name for a type that conforms to the [`conversationAttribute`](../messagesenum/conversationattribute.md) enum schema, which your app defines and implements. |
| `dateLastActive` | `Date?` | Foundation | Date |

## See Also

### Content and parameter types
- [var customAttachment: some AppSchemaEntity](./customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](./message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](./messageperson.md)
  An entity schema for a message person.
- [AppSchema.MessagesEntity](../messagesentity.md)
  Identifies entity schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity/conversation)*
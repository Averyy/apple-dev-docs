# conversation

**Framework**: App Intents  
**Kind**: property

An entity schema for a conversation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var conversation: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `messages` domain and its content matches the `conversation` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .messages.conversation)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `conversation` schema:

```swift
@AppEntity(schema: .messages.conversation)
struct ConversationEntity {
    // MARK: Static

    static let defaultQuery = ConversationEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var recipients: [<#MessagePerson#>]
    var displayName: String
    var previewText: AttributedString
    var conversationName: String?
    var isRead: Bool
    var attributes: Set<<#ConversationAttribute#>>
    var dateLastActive: Date?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

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

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var customAttachment: some AppSchemaEntity](appschema/messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](appschema/messagesentity/message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](appschema/messagesentity/messageperson.md)
  An entity schema for a message person.
- [AppSchema.MessagesEntity](appschema/messagesentity.md)
  Identifies entity schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity/conversation)*
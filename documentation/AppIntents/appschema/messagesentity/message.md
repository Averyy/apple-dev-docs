# message

**Framework**: App Intents  
**Kind**: property

An entity schema for a message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var message: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `messages` domain and its content matches the `message` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .messages.message)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `message` schema:

```swift
@AppEntity(schema: .messages.message)
struct MessageEntity {
    // MARK: Static

    static let defaultQuery = MessageEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var messageType: <#MessageType#>
    var author: <#MessagePerson#>
    var isRead: Bool
    var attributes: Set<<#MessageAttribute#>>
    var conversation: <#ConversationEntity#>
    var date: Date
    var subject: AttributedString?
    var body: AttributedString?
    var attachments: [IntentFile]
    var audioMessage: IntentFile?
    var customAttachments: [<#CustomAttachment#>]
    var locations: [GeoToolbox.PlaceDescriptor]
    var links: [LinkPresentation.LinkMetadata]
    var messageEffect: <#MessageEffect#>?
    var reaction: <#ReadReaction#>?
    var referencedMessage: <#MessageEntity#>?
    var notificationIdentifier: String?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct MessageEntityQuery: EntityQuery {
        func entities(for identifiers: [MessageEntity.ID]) async throws -> [MessageEntity] {
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

- [var conversation: some AppSchemaEntity](appschema/messagesentity/conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](appschema/messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var messagePerson: some AppSchemaEntity](appschema/messagesentity/messageperson.md)
  An entity schema for a message person.
- [AppSchema.MessagesEntity](appschema/messagesentity.md)
  Identifies entity schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity/message)*
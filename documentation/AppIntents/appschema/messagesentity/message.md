# message

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a message.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var message: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `messages` domain and its content matches the `message` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .messages.message)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `message` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `messages_message` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .messages.message)
struct MessageEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more message entities, unless you provide another.
    static let defaultQuery = MessageEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the message entity.
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

    /// The details the system shows to identify the message entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more message entities by their identifiers.
    struct MessageEntityQuery: EntityQuery {
        func entities(for identifiers: [MessageEntity.ID]) async throws -> [MessageEntity] {
            <#code#>
        }
    }
}
```

Define a `@UnionValue` enumeration for the `reaction` property, as in the following example, by typing the first few characters of `messages_readReaction` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum ReadReaction {
    case customReaction(<#CustomReaction#>)
    case attributedString(AttributedString)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the message entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `messageType` | `@AppEnum(schema: .messages.messageType)` | Your app | Type `MessageType` is a placeholder name for a type that conforms to the [`messageType`](../messagesenum/messagetype.md) enum schema, which your app defines and implements. |
| `author` | `@AppEntity(schema: .messages.messagePerson)` | Your app | Author `MessagePerson` is a placeholder name for a type that conforms to the [`messagePerson`](./messageperson.md) entity schema, which your app defines and implements. |
| `isRead` | `Bool` | Swift | Is Read |
| `attributes` | `Set<@AppEnum(schema: .messages.messageAttribute)>` | Your app | Attributes `MessageAttribute` is a placeholder name for a type that conforms to the [`messageAttribute`](../messagesenum/messageattribute.md) enum schema, which your app defines and implements. |
| `conversation` | `@AppEntity(schema: .messages.conversation)` | Your app | Conversation `ConversationEntity` is a placeholder name for a type that conforms to the [`conversation`](./conversation.md) entity schema, which your app defines and implements. |
| `date` | `Date` | Foundation | Date |
| `subject` | `AttributedString?` | Foundation | Subject |
| `body` | `AttributedString?` | Foundation | Body |
| `attachments` | `[IntentFile]` | App Intents | Attachments |
| `audioMessage` | `IntentFile?` | App Intents | Audio Message |
| `customAttachments` | `[@AppEntity(schema: .messages.customAttachment)]` | Your app | Custom Attachments `CustomAttachment` is a placeholder name for a type that conforms to the [`customAttachment`](./customattachment.md) entity schema, which your app defines and implements. |
| `locations` | `[GeoToolbox.PlaceDescriptor]` | GeoToolbox | Locations |
| `links` | `[LinkPresentation.LinkMetadata]` | LinkPresentation | Links |
| `messageEffect` | `@AppEnum(schema: .messages.messageEffect)?` | Your app | Effect `MessageEffect` is a placeholder name for a type that conforms to the [`messageEffect`](../messagesenum/messageeffect.md) enum schema, which your app defines and implements. |
| `reaction` | `@UnionValue?` | Your app | Reaction `ReadReaction` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `referencedMessage` | `@AppEntity(schema: .messages.message)?` | Your app | Reference `MessageEntity` is a placeholder name for a type that conforms to the [`message`](./message.md) entity schema, which your app defines and implements. |
| `notificationIdentifier` | `String?` | Swift | Notification |

## See Also

### Content and parameter types
- [var conversation: some AppSchemaEntity](./conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](./customattachment.md)
  An entity schema for a custom attachment.
- [var messagePerson: some AppSchemaEntity](./messageperson.md)
  An entity schema for a message person.
- [AppSchema.MessagesEntity](../messagesentity.md)
  Identifies entity schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity/message)*
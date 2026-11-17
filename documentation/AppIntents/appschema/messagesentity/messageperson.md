# messagePerson

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a message person.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var messagePerson: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `messages` domain and its content matches the `messagePerson` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .messages.messagePerson)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `messagePerson` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `messages_messagePerson` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .messages.messagePerson)
struct MessagePerson {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more person entities, unless you provide another.
    static let defaultQuery = MessagePersonQuery()

    // MARK: Entity properties

    /// The unique identifier for the person entity.
    let id: <#Identifiable.ID#>

    var person: IntentPerson

    /// The details the system shows to identify the person entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more person entities by their identifiers.
    struct MessagePersonQuery: EntityQuery {
        func entities(for identifiers: [MessagePerson.ID]) async throws -> [MessagePerson] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the message-person entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `person` | `IntentPerson` | App Intents | Person |

## See Also

### Content and parameter types
- [var conversation: some AppSchemaEntity](./conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](./customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](./message.md)
  An entity schema for a message.
- [AppSchema.MessagesEntity](../messagesentity.md)
  Identifies entity schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity/messageperson)*
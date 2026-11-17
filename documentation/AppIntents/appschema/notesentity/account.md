# account

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an account.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var account: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `notes` domain and its content matches the `account` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .notes.account)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `account` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `notes_account` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .notes.account)
struct AccountEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more account entities, unless you provide another.
    static let defaultQuery = AccountEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the account entity.
    let id: <#Identifiable.ID#>

    var name: String

    /// The details the system shows to identify the account entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more account entities by their identifiers.
    struct AccountEntityQuery: EntityQuery {
        func entities(for identifiers: [AccountEntity.ID]) async throws -> [AccountEntity] {
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

## See Also

### Content and parameter types
- [var folder: some AppSchemaEntity](./folder.md)
  An entity schema for a folder.
- [var note: some AppSchemaEntity](./note.md)
  An entity schema for a note.
- [AppSchema.NotesEntity](../notesentity.md)
  Identifies entity schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesentity/account)*
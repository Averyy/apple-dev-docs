# folder

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a folder.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var folder: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `notes` domain and its content matches the `folder` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .notes.folder)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `folder` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `notes_folder` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .notes.folder)
struct FolderEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more folder entities, unless you provide another.
    static let defaultQuery = FolderEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the folder entity.
    let id: <#Identifiable.ID#>

    var name: String

    var parentFolder: <#FolderEntity#>?

    var account: <#AccountEntity#>?

    /// The details the system shows to identify the folder entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more folder entities by their identifiers.
    struct FolderEntityQuery: EntityQuery {
        func entities(for identifiers: [FolderEntity.ID]) async throws -> [FolderEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the folder entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |
| `parentFolder` | `@AppEntity(schema: .notes.folder)?` | Your app | Parent Folder `FolderEntity` is a placeholder name for a type that conforms to the [`folder`](./folder.md) entity schema, which your app defines and implements. |
| `account` | `@AppEntity(schema: .notes.account)?` | Your app | Account `AccountEntity` is a placeholder name for a type that conforms to the [`account`](./account.md) entity schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var account: some AppSchemaEntity](./account.md)
  An entity schema for an account.
- [var note: some AppSchemaEntity](./note.md)
  An entity schema for a note.
- [AppSchema.NotesEntity](../notesentity.md)
  Identifies entity schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesentity/folder)*
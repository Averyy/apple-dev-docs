# note

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a note.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var note: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `notes` domain and its content matches the `note` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .notes.note)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `note` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `notes_note` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .notes.note)
struct NoteEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more note entities, unless you provide another.
    static let defaultQuery = NoteEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the note entity.
    let id: <#Identifiable.ID#>

    var name: AttributedString

    var content: AttributedString?

    var attachments: [IntentFile]

    var isPinned: Bool

    var creationDate: Date?

    var modificationDate: Date?

    var folder: <#FolderEntity#>?

    /// The details the system shows to identify the note entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more note entities by their identifiers.
    struct NoteEntityQuery: EntityQuery {
        func entities(for identifiers: [NoteEntity.ID]) async throws -> [NoteEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the note entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `AttributedString` | Foundation | Name |
| `content` | `AttributedString?` | Foundation | Content |
| `attachments` | `[IntentFile]` | App Intents | Attachments |
| `isPinned` | `Bool` | Swift | Is Pinned |
| `creationDate` | `Date?` | Foundation | Creation Date |
| `modificationDate` | `Date?` | Foundation | Modification Date |
| `folder` | `@AppEntity(schema: .notes.folder)?` | Your app | Folder `FolderEntity` is a placeholder name for a type that conforms to the [`folder`](./folder.md) entity schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var account: some AppSchemaEntity](./account.md)
  An entity schema for an account.
- [var folder: some AppSchemaEntity](./folder.md)
  An entity schema for a folder.
- [AppSchema.NotesEntity](../notesentity.md)
  Identifies entity schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesentity/note)*
# folder

**Framework**: App Intents  
**Kind**: property

An entity schema for a folder.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var folder: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `notes` domain and its content matches the `folder` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .notes.folder)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `folder` schema:

```swift
@AppEntity(schema: .notes.folder)
struct FolderEntity {
    // MARK: Static

    static let defaultQuery = FolderEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var parentFolder: <#FolderEntity#>?
    var account: <#AccountEntity#>?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

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

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var account: some AppSchemaEntity](appschema/notesentity/account.md)
  An entity schema for an account.
- [var note: some AppSchemaEntity](appschema/notesentity/note.md)
  An entity schema for a note.
- [var tag: some AppSchemaEntity](appschema/notesentity/tag.md)
  An entity schema for a tag.
- [AppSchema.NotesEntity](appschema/notesentity.md)
  Identifies entity schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesentity/folder)*
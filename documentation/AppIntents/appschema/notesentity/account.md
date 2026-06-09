# account

**Framework**: App Intents  
**Kind**: property

An entity schema for an account.

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
var account: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `notes` domain and its content matches the `account` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .notes.account)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `account` schema:

```swift
@AppEntity(schema: .notes.account)
struct AccountEntity {
    // MARK: Static

    static let defaultQuery = AccountEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

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

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var folder: some AppSchemaEntity](appschema/notesentity/folder.md)
  An entity schema for a folder.
- [var note: some AppSchemaEntity](appschema/notesentity/note.md)
  An entity schema for a note.
- [var tag: some AppSchemaEntity](appschema/notesentity/tag.md)
  An entity schema for a tag.
- [AppSchema.NotesEntity](appschema/notesentity.md)
  Identifies entity schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesentity/account)*
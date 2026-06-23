# file

**Framework**: App Intents  
**Kind**: property

An entity schema for a file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var file: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `files` domain and its content matches the `file` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .files.file)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `file` schema:

```swift
@AppEntity(schema: .files.file)
struct FileEntity: FileEntity {
    // MARK: Static

    static let defaultQuery = FileEntityQuery()
    static var supportedContentTypes = [<#UTType#>]

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var creationDate: Date?
    var fileModificationDate: Date?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct FileEntityQuery: EntityQuery {
        func entities(for identifiers: [FileEntity.ID]) async throws -> [FileEntity] {
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

- [AppSchema.FilesEntity](appschema/filesentity.md)
  Identifies entity schemas in the files domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/filesentity/file)*
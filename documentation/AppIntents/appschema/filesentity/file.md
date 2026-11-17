# file

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var file: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `files` domain and its content matches the `file` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .files.file)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `file` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `files_file` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .files.file)
struct FilesFileEntity: FileEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more file entities, unless you provide another.
    static let defaultQuery = FilesFileEntityQuery()
    static var supportedContentTypes = [<#UTType#>]

    // MARK: Entity properties

    /// The unique identifier for the file entity.
    let id: <#Identifiable.ID#>

    var creationDate: Date?

    var fileModificationDate: Date?

    /// The details the system shows to identify the file entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more file entities by their identifiers.
    struct FilesFileEntityQuery: EntityQuery {
        func entities(for identifiers: [FilesFileEntity.ID]) async throws -> [FilesFileEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the file entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `creationDate` | `Date?` | Foundation | Creation Date |
| `fileModificationDate` | `Date?` | Foundation | Last Modification Date |

## See Also

### Content and parameter types
- [AppSchema.FilesEntity](../filesentity.md)
  Identifies entity schemas in the files domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/filesentity/file)*
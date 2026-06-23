# document

**Framework**: App Intents  
**Kind**: property

An entity schema for a document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var document: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reader` domain and its content matches the `document` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .reader.document)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `document` schema:

```swift
@AppEntity(schema: .reader.document)
struct ReaderDocumentEntity {
    // MARK: Static

    static let defaultQuery = ReaderDocumentEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String
    var kind: <#ReaderDocumentKind#>
    var width: Int?
    var height: Int?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct ReaderDocumentEntityQuery: EntityQuery {
        func entities(for identifiers: [ReaderDocumentEntity.ID]) async throws -> [ReaderDocumentEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var page: some AppSchemaEntity](appschema/readerentity/page.md)
  An entity schema for a page.
- [AppSchema.ReaderEntity](appschema/readerentity.md)
  Identifies entity schemas in the reader domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerentity/document)*
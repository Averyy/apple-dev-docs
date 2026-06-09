# document

**Framework**: App Intents  
**Kind**: property

An entity schema for a document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var document: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `wordProcessor` domain and its content matches the `document` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .wordProcessor.document)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `document` schema:

```swift
@AppEntity(schema: .wordProcessor.document)
struct WordProcessorDocumentEntity {
    // MARK: Static

    static let defaultQuery = WordProcessorDocumentEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var creationDate: Date?
    var modificationDate: Date?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct WordProcessorDocumentEntityQuery: EntityQuery {
        func entities(for identifiers: [WordProcessorDocumentEntity.ID]) async throws -> [WordProcessorDocumentEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var page: some AppSchemaEntity](appschema/wordprocessorentity/page.md)
  An entity schema for a page.
- [var template: some AppSchemaEntity](appschema/wordprocessorentity/template.md)
  An entity schema for a template.
- [AppSchema.WordProcessorEntity](appschema/wordprocessorentity.md)
  Identifies entity schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorentity/document)*
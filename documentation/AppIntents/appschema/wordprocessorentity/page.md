# page

**Framework**: App Intents  
**Kind**: property

An entity schema for a page.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var page: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `wordProcessor` domain and its content matches the `page` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .wordProcessor.page)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `page` schema:

```swift
@AppEntity(schema: .wordProcessor.page)
struct WordProcessorPageEntity {
    // MARK: Static

    static let defaultQuery = WordProcessorPageEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var document: <#WordProcessorDocumentEntity#>
    var pageIndex: Int

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct WordProcessorPageEntityQuery: EntityQuery {
        func entities(for identifiers: [WordProcessorPageEntity.ID]) async throws -> [WordProcessorPageEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var document: some AppSchemaEntity](appschema/wordprocessorentity/document.md)
  An entity schema for a document.
- [var template: some AppSchemaEntity](appschema/wordprocessorentity/template.md)
  An entity schema for a template.
- [AppSchema.WordProcessorEntity](appschema/wordprocessorentity.md)
  Identifies entity schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorentity/page)*
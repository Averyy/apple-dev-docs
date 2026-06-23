# template

**Framework**: App Intents  
**Kind**: property

An entity schema for a template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var template: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `wordProcessor` domain and its content matches the `template` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .wordProcessor.template)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `template` schema:

```swift
@AppEntity(schema: .wordProcessor.template)
struct WordProcessorDocumentTemplateEntity {
    // MARK: Static

    static let defaultQuery = WordProcessorDocumentTemplateEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct WordProcessorDocumentTemplateEntityQuery: EntityQuery {
        func entities(for identifiers: [WordProcessorDocumentTemplateEntity.ID]) async throws -> [WordProcessorDocumentTemplateEntity] {
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
- [var page: some AppSchemaEntity](appschema/wordprocessorentity/page.md)
  An entity schema for a page.
- [AppSchema.WordProcessorEntity](appschema/wordprocessorentity.md)
  Identifies entity schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorentity/template)*
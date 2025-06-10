# document

**Framework**: App Intents  
**Kind**: property

The app entity describes a document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var document: some AssistantSchemas.Entity { get }
```

## Mentions

- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation The following example shows an app entity that conforms to the `.reader.document` schema:

```swift
@AssistantEntity(schema: .reader.document)
struct ReaderDocumentEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [ReaderDocumentEntity.ID]) async throws -> [ReaderDocumentEntity] { [] }
        func entities(matching string: String) async throws -> [ReaderDocumentEntity] { [] }
    }
    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Document" }

    let id = UUID()

    @Property
    var title: String

    @Property
    var kind: ReaderDocumentKind

    @Property
    var width: Int?

    @Property
    var height: Int?
}
```

For more information about the `.reader` app intent domain, see [`Making document reader actions available to Siri and Apple Intelligence`](making-document-reader-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerentity/document)*
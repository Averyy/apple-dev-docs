# document

**Framework**: App Intents  
**Kind**: property

The app entity describes a text document.

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

- [Making word processor actions available to Siri and Apple Intelligence](making-word-processor-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.The following example shows an app entity that conforms to the `.wordProcessor.document` schema:

```swift
@AssistantEntity(schema: .wordProcessor.document)
struct WordProcessorDocumentEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [WordProcessorDocumentEntity.ID]) async throws -> [WordProcessorDocumentEntity] { [] }
        func entities(matching string: String) async throws -> [WordProcessorDocumentEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Text Document" }

    let id = UUID()

    @Property
    var name: String

    @Property
    var creationDate: Date?

    @Property
    var modificationDate: Date?
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/wordprocessorentity/document)*
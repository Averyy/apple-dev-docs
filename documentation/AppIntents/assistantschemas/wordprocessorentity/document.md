# document

**Framework**: App Intents  
**Kind**: property

The app entity describes a text document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
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

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.wordProcessor` app intent domain, see [`Making word processor actions available to Siri and Apple Intelligence`](making-word-processor-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.wordProcessor.document` schema:

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
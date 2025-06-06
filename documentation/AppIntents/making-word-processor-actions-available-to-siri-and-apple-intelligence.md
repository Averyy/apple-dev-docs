# Making word processor actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities that make your app’s word processor functionality available to Siri and Apple Intelligence.

#### Overview

To integrate your app’s word processor capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app entity implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows someone to open a text document, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.wordProcessor` domain and the [`open`](assistantschemas/wordprocessorintent/open.md) schema:

```swift
@AssistantIntent(schema: .wordProcessor.open)
struct OpenWordProcessorDocumentIntent: OpenIntent {
    var target: WordProcessorDocumentEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.wordProcessor` domain, see [`AssistantSchemas.WordProcessorIntent`](assistantschemas/wordprocessorintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `DocumentEntity`. The following code snippet shows how the `DocumentEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AssistantEntity(schema: .wordProcessor.document)
struct WordProcessorDocumentEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [WordProcessorDocumentEntity.ID]) async throws -> [WordProcessorDocumentEntity] { [] }
        func entities(matching string: String) async throws -> [WordProcessorDocumentEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Provide a display representation." }

    let id = UUID()

    var name: String
    var creationDate: Date?
    var modificationDate: Date?
}
```

The assistant schema for the `DocumentEntity` consists of the `.wordProcessor` domain and the [`document`](assistantschemas/wordprocessorentity/document.md) schema.

For a list of available app entity schemas in the `.wordProcessor` domain, see [`AssistantSchemas.WordProcessorEntity`](assistantschemas/wordprocessorentity.md).

## See Also

- [AssistantSchemas.WordProcessorIntent](assistantschemas/wordprocessorintent.md)
  Assistant schema conformance for app intents that offer word processing functionality.
- [AssistantSchemas.WordProcessorEntity](assistantschemas/wordprocessorentity.md)
  Assistant schema conformance for app entities that describe text documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-word-processor-actions-available-to-siri-and-apple-intelligence)*
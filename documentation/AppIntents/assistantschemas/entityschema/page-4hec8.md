# page

**Framework**: App Intents  
**Kind**: property

The app entity describes a page in a text document.

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
var page: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.wordProcessor` app intent domain, see [`Making word processor actions available to Siri and Apple Intelligence`](making-word-processor-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.wordProcessor.page` schema:

```swift
@AssistantEntity(schema: .wordProcessor.page)
struct WordProcessorPageEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [WordProcessorPageEntity.ID]) async throws -> [WordProcessorPageEntity] { [] }
        func entities(matching string: String) async throws -> [WordProcessorPageEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Text Document Page" }

    let id = UUID()

    @Property
    var document: WordProcessorDocumentEntity

    @Property
    var pageIndex: Int
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entityschema/page-4hec8)*
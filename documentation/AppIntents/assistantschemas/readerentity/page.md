# page

**Framework**: App Intents  
**Kind**: property

The app entity describes a page.

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
var page: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.reader.page` schema:

```swift
@AssistantEntity(schema: .reader.page)
struct ReaderPageEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [ReaderPageEntity.ID]) async throws -> [ReaderPageEntity] { [] }
        func entities(matching string: String) async throws -> [ReaderPageEntity] { [] }
    }
    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Page" }

    let id = UUID()

    @Property var label: String
}
```

For more information about the `.reader` app intent domain, see [`Making document reader actions available to Siri and Apple Intelligence`](making-document-reader-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerentity/page)*
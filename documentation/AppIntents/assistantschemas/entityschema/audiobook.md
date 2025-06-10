# audiobook

**Framework**: App Intents  
**Kind**: property

The app entity describes an audiobook.

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
var audiobook: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.books.audiobook` schema:

```swift
@AssistantEntity(schema: .books.audiobook)
struct AudiobookEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [AudiobookEntity.ID]) async throws -> [AudiobookEntity] { [] }
        func entities(matching string: String) async throws -> [AudiobookEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Audiobook" }

    let id = UUID()

    @Property
    var title: String?

    @Property
    var seriesTitle: String?

    @Property
    var author: String?

    @Property
    var genre: String?

    @Property
    var purchaseDate: Date?
}
```

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entityschema/audiobook)*
# book

**Framework**: App Intents  
**Kind**: property

The app entity describes an ebook.

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
var book: some AssistantSchemas.Entity { get }
```

## Mentions

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.books.book` schema:

```swift
@AppEntity(schema: .books.book)
struct BookEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [BookEntity.ID]) async throws -> [BookEntity] { [] }
        func entities(matching string: String) async throws -> [BookEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Book" }

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

    @Property
    var contentType: BookContentType?
}
```

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksentity/book)*
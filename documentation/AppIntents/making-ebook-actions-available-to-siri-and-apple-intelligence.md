# Making ebook actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s ebook and audiobook functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s ebook and audiobook capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent, app entity, and app enumeration implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows a person to open an ebook, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.books` domain and the [`openBook`](assistantschemas/booksintent/openbook.md) schema:

```swift
@AssistantIntent(schema: .books.openBook)
struct OpenBookIntent: OpenIntent {
    var target: BookEntity
    
    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.books` domain, see [`AssistantSchemas.BooksIntent`](assistantschemas/booksintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `BookEntity`. The following code snippet shows how the `BookEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AssistantEntity(schema: .books.book)
struct BookEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [BookEntity.ID]) async throws -> [BookEntity] { [] }
        func entities(matching string: String) async throws -> [BookEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Provide a display representation." }
    
    let id = UUID()
    
    var title: String?
    var seriesTitle: String?
    var author: String?
    var genre: String?
    var purchaseDate: Date?
    var contentType: BookContentType?
    var url: URL?
}
```

The assistant schema for the `BookEntity` consists of the `.books` domain and the [`book`](assistantschemas/booksentity/book.md) schema.

For a list of available app entity schemas in the `.books` domain, see [`AssistantSchemas.BooksEntity`](assistantschemas/booksentity.md).

##### Make Sure Your Enumeration Meets Requirements

To make sure Siri and Apple Intelligence understand custom static types for your intent parameters, annotate app enumerations with the [`AssistantEnum(schema:)`](assistantenum(schema:).md) macro. Then, pass the `.books` domain and a schema to it. The following example uses the [`contentType`](assistantschemas/booksenum/contenttype.md) schema:

```swift
@AssistantEnum(schema: .books.contentType)
enum BookContentType: String, AppEnum {
    case book
    case pdf

    static var caseDisplayRepresentations: [BookContentType: AppIntents.DisplayRepresentation] = [:]

}
```

For a list of available app enumeration schemas in the `.books` domain, see [`AssistantSchemas.BooksEnum`](assistantschemas/booksenum.md).

## See Also

- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.
- [AssistantSchemas.BooksEntity](assistantschemas/booksentity.md)
  Assistant schema conformance for app entities that describe ebooks or audiobooks.
- [AssistantSchemas.BooksEnum](assistantschemas/booksenum.md)
  Assistant schema conformance for types you use to describe ebooks or audiobooks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-ebook-actions-available-to-siri-and-apple-intelligence)*
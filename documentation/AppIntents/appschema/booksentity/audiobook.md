# audiobook

**Framework**: App Intents  
**Kind**: property

An entity schema for an audiobook.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var audiobook: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `books` domain and its content matches the `audiobook` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .books.audiobook)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `audiobook` schema:

```swift
@AppEntity(schema: .books.audiobook)
struct AudiobookEntity {
    // MARK: Static

    static let defaultQuery = AudiobookEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String?
    var seriesTitle: String?
    var author: String?
    var genre: String?
    var purchaseDate: Date?
    var url: URL?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct AudiobookEntityQuery: EntityQuery {
        func entities(for identifiers: [AudiobookEntity.ID]) async throws -> [AudiobookEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var book: some AppSchemaEntity](appschema/booksentity/book.md)
  An entity schema for a book.
- [var settings: some AppSchemaEntity](appschema/booksentity/settings.md)
  An entity schema for  settings.
- [AppSchema.BooksEntity](appschema/booksentity.md)
  Identifies entity schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksentity/audiobook)*
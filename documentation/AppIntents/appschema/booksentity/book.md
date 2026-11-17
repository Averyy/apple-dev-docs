# book

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a book.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var book: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `books` domain and its content matches the `book` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .books.book)` Swift macro.

The following example shows an app entity that conforms to the `book` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_book` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .books.book)
struct BookEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more book entities, unless you provide another.
    static let defaultQuery = BookEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the book entity.
    let id: <#Identifiable.ID#>

    var title: String?

    var seriesTitle: String?

    var author: String?

    var genre: String?

    var purchaseDate: Date?

    var url: URL?

    /// The details the system shows to identify the book entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more book entities by their identifiers.
    struct BookEntityQuery: EntityQuery {
        func entities(for identifiers: [BookEntity.ID]) async throws -> [BookEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the book entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String?` | Swift | Title |
| `seriesTitle` | `String?` | Swift | Series Title |
| `author` | `String?` | Swift | Author |
| `genre` | `String?` | Swift | Genre |
| `purchaseDate` | `Date?` | Foundation | Date of Purchase |
| `url` | `URL?` | Foundation | URL |

## See Also

### Content and parameter types
- [var audiobook: some AppSchemaEntity](./audiobook.md)
  An entity schema for an audiobook.
- [var settings: some AppSchemaEntity](./settings.md)
  An entity schema for settings.
- [AppSchema.BooksEntity](../booksentity.md)
  Identifies entity schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksentity/book)*
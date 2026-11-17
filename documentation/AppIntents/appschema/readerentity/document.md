# document

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var document: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reader` domain and its content matches the `document` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .reader.document)` Swift macro.

The following example shows an app entity that conforms to the `document` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reader_document` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .reader.document)
struct ReaderDocumentEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more document entities, unless you provide another.
    static let defaultQuery = ReaderDocumentEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the document entity.
    let id: <#Identifiable.ID#>

    var title: String

    var kind: <#ReaderDocumentKind#>

    var width: Int?

    var height: Int?

    /// The details the system shows to identify the document entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more document entities by their identifiers.
    struct ReaderDocumentEntityQuery: EntityQuery {
        func entities(for identifiers: [ReaderDocumentEntity.ID]) async throws -> [ReaderDocumentEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the document entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Title |
| `kind` | `@AppEnum(schema: .reader.documentKind)` | Your app | Kind `ReaderDocumentKind` is a placeholder name for a type that conforms to the [`documentKind`](../readerenum/documentkind.md) enum schema, which your app defines and implements. |
| `width` | `Int?` | Swift | Width |
| `height` | `Int?` | Swift | Height |

## See Also

### Content and parameter types
- [var page: some AppSchemaEntity](./page.md)
  An entity schema for a page.
- [AppSchema.ReaderEntity](../readerentity.md)
  Identifies entity schemas in the reader domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerentity/document)*
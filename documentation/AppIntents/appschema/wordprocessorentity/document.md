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

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `wordProcessor` domain and its content matches the `document` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .wordProcessor.document)` Swift macro.

The following example shows an app entity that conforms to the `document` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `wordProcessor_document` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .wordProcessor.document)
struct WordProcessorDocumentEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more document entities, unless you provide another.
    static let defaultQuery = WordProcessorDocumentEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the document entity.
    let id: <#Identifiable.ID#>

    var name: String

    var creationDate: Date?

    var modificationDate: Date?

    /// The details the system shows to identify the document entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more document entities by their identifiers.
    struct WordProcessorDocumentEntityQuery: EntityQuery {
        func entities(for identifiers: [WordProcessorDocumentEntity.ID]) async throws -> [WordProcessorDocumentEntity] {
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
| `name` | `String` | Swift | Name |
| `creationDate` | `Date?` | Foundation | Creation Date |
| `modificationDate` | `Date?` | Foundation | Modification Date |

## See Also

### Content and parameter types
- [var page: some AppSchemaEntity](./page.md)
  An entity schema for a page.
- [var template: some AppSchemaEntity](./template.md)
  An entity schema for a template.
- [AppSchema.WordProcessorEntity](../wordprocessorentity.md)
  Identifies entity schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorentity/document)*
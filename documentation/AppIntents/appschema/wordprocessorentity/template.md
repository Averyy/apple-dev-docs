# template

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var template: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `wordProcessor` domain and its content matches the `template` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .wordProcessor.template)` Swift macro.

The following example shows an app entity that conforms to the `template` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `wordProcessor_template` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .wordProcessor.template)
struct WordProcessorDocumentTemplateEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more template entities, unless you provide another.
    static let defaultQuery = WordProcessorDocumentTemplateEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the template entity.
    let id: <#Identifiable.ID#>

    var name: String

    /// The details the system shows to identify the template entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more template entities by their identifiers.
    struct WordProcessorDocumentTemplateEntityQuery: EntityQuery {
        func entities(for identifiers: [WordProcessorDocumentTemplateEntity.ID]) async throws -> [WordProcessorDocumentTemplateEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the template entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |

## See Also

### Content and parameter types
- [var document: some AppSchemaEntity](./document.md)
  An entity schema for a document.
- [var page: some AppSchemaEntity](./page.md)
  An entity schema for a page.
- [AppSchema.WordProcessorEntity](../wordprocessorentity.md)
  Identifies entity schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorentity/template)*
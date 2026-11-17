# page

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a page.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var page: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reader` domain and its content matches the `page` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .reader.page)` Swift macro.

The following example shows an app entity that conforms to the `page` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reader_page` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .reader.page)
struct ReaderPageEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more page entities, unless you provide another.
    static let defaultQuery = ReaderPageEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the page entity.
    let id: <#Identifiable.ID#>

    var label: String

    /// The details the system shows to identify the page entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more page entities by their identifiers.
    struct ReaderPageEntityQuery: EntityQuery {
        func entities(for identifiers: [ReaderPageEntity.ID]) async throws -> [ReaderPageEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the page entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `label` | `String` | Swift | Label |

## See Also

### Content and parameter types
- [var document: some AppSchemaEntity](./document.md)
  An entity schema for a document.
- [AppSchema.ReaderEntity](../readerentity.md)
  Identifies entity schemas in the reader domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerentity/page)*
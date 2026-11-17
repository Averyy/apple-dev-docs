# slide

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a slide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var slide: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `presentation` domain and its content matches the `slide` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .presentation.slide)` Swift macro.

The following example shows an app entity that conforms to the `slide` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `presentation_slide` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .presentation.slide)
struct PresentationSlideEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more slide entities, unless you provide another.
    static let defaultQuery = PresentationSlideEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the slide entity.
    let id: <#Identifiable.ID#>

    var presentation: <#PresentationEntity#>

    var slideIndex: Int?

    var title: String?

    /// The details the system shows to identify the slide entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more slide entities by their identifiers.
    struct PresentationSlideEntityQuery: EntityQuery {
        func entities(for identifiers: [PresentationSlideEntity.ID]) async throws -> [PresentationSlideEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the slide entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `presentation` | `@AppEntity(schema: .presentation.document)` | Your app | Presentation `PresentationEntity` is a placeholder name for a type that conforms to the [`document`](./document.md) entity schema, which your app defines and implements. |
| `slideIndex` | `Int?` | Swift | Position |
| `title` | `String?` | Swift | Title |

## See Also

### Content and parameter types
- [var document: some AppSchemaEntity](./document.md)
  An entity schema for a document.
- [var template: some AppSchemaEntity](./template.md)
  An entity schema for a template.
- [AppSchema.PresentationEntity](../presentationentity.md)
  Identifies entity schemas in the presentation domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationentity/slide)*
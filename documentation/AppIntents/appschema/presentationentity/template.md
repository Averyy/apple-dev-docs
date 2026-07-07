# template

**Framework**: App Intents  
**Kind**: property

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

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `presentation` domain and its content matches the `template` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .presentation.template)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `template` schema:

```swift
@AppEntity(schema: .presentation.template)
struct PresentationTemplateEntity {
    // MARK: Static

    static let defaultQuery = PresentationTemplateEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct PresentationTemplateEntityQuery: EntityQuery {
        func entities(for identifiers: [PresentationTemplateEntity.ID]) async throws -> [PresentationTemplateEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var document: some AppSchemaEntity](appschema/presentationentity/document.md)
  An entity schema for a document.
- [var slide: some AppSchemaEntity](appschema/presentationentity/slide.md)
  An entity schema for a slide.
- [AppSchema.PresentationEntity](appschema/presentationentity.md)
  Identifies entity schemas in the presentation domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationentity/template)*
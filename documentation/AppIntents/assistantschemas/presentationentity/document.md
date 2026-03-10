# document

**Framework**: App Intents  
**Kind**: property

The app entity describes a presentation.

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
var document: some AssistantSchemas.Entity { get }
```

## Mentions

- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.presentation.document` schema:

```swift
@AppEntity(schema: .presentation.document)
struct PresentationEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PresentationEntity.ID]) async throws -> [PresentationEntity] { [] }
        func entities(matching string: String) async throws -> [PresentationEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Presentation" }

    let id = UUID()

    @Property
    var name: String
}
```

For more information about the `.presentation` app intent domain, see [`Making presentation actions available to Siri and Apple Intelligence`](making-presentation-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var slide: some AssistantSchemas.Entity](assistantschemas/presentationentity/slide.md)
  The app entity describes a slide.
- [var template: some AssistantSchemas.Entity](assistantschemas/presentationentity/template.md)
  The app entity describes a template for a presentation.
- [AssistantSchemas.PresentationEntity](assistantschemas/presentationentity.md)
  Assistant schema conformance for app entities that describe presentation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationentity/document)*
# template

**Framework**: App Intents  
**Kind**: property

The app entity describes a template for a presentation.

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
var template: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.presentation.template` schema:

```swift
@AssistantEntity(schema: .presentation.template)
struct PresentationTemplateEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PresentationTemplateEntity.ID]) async throws -> [PresentationTemplateEntity] { [] }
        func entities(matching string: String) async throws -> [PresentationTemplateEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Presentation Template" }

    let id = UUID()

    @Property
    var name: String
}
```

For more information about the `.presentation` app intent domain, see [`Making presentation actions available to Siri and Apple Intelligence`](making-presentation-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entityschema/template-7r2rr)*
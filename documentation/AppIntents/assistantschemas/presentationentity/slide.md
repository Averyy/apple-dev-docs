# slide

**Framework**: App Intents  
**Kind**: property

The app entity describes a slide.

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
var slide: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.presentation.slide` schema:

```swift
@AppEntity(schema: .presentation.slide)
struct PresentationSlideEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PresentationSlideEntity.ID]) async throws -> [PresentationSlideEntity] { [] }
        func entities(matching string: String) async throws -> [PresentationSlideEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Presentation Slide" }

    let id = UUID()

    @Property
    var presentation: PresentationEntity

    @Property
    var slideIndex: Int?

    @Property
    var title: String?
}
```

For more information about the `.presentation` app intent domain, see doc:Making-presentation-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationentity/slide)*
# Making presentation actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s presentation functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s presentation capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app entity implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows someone to open a presentation, use the [`AppIntent(schema:)`](appintent(schema:).md) macro and provide the assistant schema that consists of the `.presentation` domain and the [`createSlide`](assistantschemas/presentationintent/createslide.md) schema:

```swift
@AppIntent(schema: .presentation.open)
struct OpenPresentationIntent: OpenIntent {
    var target: PresentationEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.presentation` domain, see [`AssistantSchemas.PresentationIntent`](assistantschemas/presentationintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AppEntity(schema:)`](appentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `PresentationEntity`. The following code snippet shows how the `PresentationEntity` implementation uses the [`AppEntity(schema:)`](appentity(schema:).md) macro:

```swift
@AppEntity(schema: .presentation.document)
struct PresentationEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PresentationEntity.ID]) async throws -> [PresentationEntity] { [] }
        func entities(matching string: String) async throws -> [PresentationEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Provide a display representation." }

    let id = UUID()

    var name: String
}
```

The assistant schema for the `PresentationEntity` consists of the `.presentation` domain and the [`document`](assistantschemas/presentationentity/document.md) schema.

For a list of available app entity schemas in the `.presentation` domain, see [`AssistantSchemas.PresentationEntity`](assistantschemas/presentationentity.md).

## See Also

- [AssistantSchemas.PresentationIntent](assistantschemas/presentationintent.md)
  Assistant schema conformance for app intents that offer presentation functionality.
- [AssistantSchemas.PresentationEntity](assistantschemas/presentationentity.md)
  Assistant schema conformance for app entities that describe presentation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-presentation-actions-available-to-siri-and-apple-intelligence)*
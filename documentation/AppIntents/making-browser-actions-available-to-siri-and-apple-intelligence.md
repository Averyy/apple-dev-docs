# Making browser actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s web browsing functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s web browsing functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent, app entity, and app enumeration implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows a person to open a website in a new tab, use the [`AppIntent(schema:)`](appintent(schema:).md) macro and provide the assistant schema that consists of the `.browser` domain and the [`createTab`](assistantschemas/browserintent/createtab.md) schema:

```swift
@AppIntent(schema: .browser.createTab)
struct CreateTabIntent: AppIntent {
    var url: URL?
    var isPrivate: Bool

    // Return a TabEntity instance.
    func perform() async throws -> some ReturnsValue<TabEntity> {
       .result(value: TabEntity())
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.browser` domain, see [`AssistantSchemas.BrowserIntent`](assistantschemas/browserintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AppEntity(schema:)`](appentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `TabEntity`. The following code snippet shows how the `TabEntity` implementation uses the [`AppEntity(schema:)`](appentity(schema:).md) macro:

```swift
@AppEntity(schema: .browser.tab)
struct TabEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [TabEntity.ID]) async throws -> [TabEntity] { [] }
        func entities(matching string: String) async throws -> [TabEntity] { [] }
    }
    static var defaultQuery = Query()
    
    var displayRepresentation: AppIntents.DisplayRepresentation { "TabEntity" }

    let id = UUID()

    var url: URL?
    var name: String
    var isPrivate: Bool
}
```

The assistant schema for the `TabEntity` consists of the `.browser` domain and the [`tab`](assistantschemas/browserentity/tab.md) schema.

For a list of available app entity schemas in the `.browser` domain, see [`AssistantSchemas.BrowserEntity`](assistantschemas/browserentity.md).

##### Make Sure Your Enumeration Meets Requirements

To make sure Siri and Apple Intelligence understand custom static types for your intent parameters, annotate app enumerations with the [`AppEnum(schema:)`](appenum(schema:).md) macro. Then, pass the `.browser` domain and a schema to it. The following example uses the [`clearHistoryTimeFrame`](assistantschemas/browserenum/clearhistorytimeframe.md) schema:

```swift
@AppEnum(schema: .browser.clearHistoryTimeFrame)
struct ClearHistoryTimeFrameEnum: String, AppEnum {
    case today
    case lastFourHours
    case todayAndYesterday
    case allTime

static var caseDisplayRepresentations: [ClearHistoryTimeFrame: DisplayRepresentation] = [:]
}
```

For a list of available app enumeration schemas in the `.browser` domain, see [`AssistantSchemas.BrowserEnum`](assistantschemas/browserenum.md).

## See Also

- [AssistantSchemas.BrowserIntent](assistantschemas/browserintent.md)
  Assistant schema conformance for app intents that offer web browsing functionality.
- [AssistantSchemas.BrowserEntity](assistantschemas/browserentity.md)
  Assistant schema conformance for app entities that describe data for web browsing functionality.
- [AssistantSchemas.BrowserEnum](assistantschemas/browserenum.md)
  Assistant schema conformance for types you use for web browsing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-browser-actions-available-to-siri-and-apple-intelligence)*
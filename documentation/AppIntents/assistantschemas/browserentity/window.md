# window

**Framework**: App Intents  
**Kind**: property

The app entity describes a browser window.

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
var window: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.browser.window` schema:

```swift
@AssistantEntity(schema: .browser.window)
struct WindowEntity: AppEntity {
    static var defaultQuery = Query()

    let id = UUID()

    @Property
    var tabs: [TabEntity]

    @Property
    var isPrivate: Bool

    var displayRepresentation: AppIntents.DisplayRepresentation { "Window" }
    struct Query: EntityStringQuery {
        func entities(for identifiers: [WindowEntity.ID]) async throws -> [WindowEntity] { [] }
        func entities(matching string: String) async throws -> [WindowEntity] { [] }
    }
}
```

For more information about the `.browser` app intent domain, see [`Making browser actions available to Siri and Apple Intelligence`](making-browser-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserentity/window)*
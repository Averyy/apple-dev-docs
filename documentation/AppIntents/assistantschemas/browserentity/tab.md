# tab

**Framework**: App Intents  
**Kind**: property

The app entity describes a browser tab.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var tab: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.browser.tab` schema:

```swift
@AppEntity(schema: .browser.tab)
struct TabEntity: AppEntity {
    static var defaultQuery = Query()

    let id = UUID()

    @Property
    var url: URL?

    @Property
    var name: String

    @Property
    var isPrivate: Bool

    var displayRepresentation: AppIntents.DisplayRepresentation { "Tab" }
    struct Query: EntityStringQuery {
        func entities(for identifiers: [TabEntity.ID]) async throws -> [TabEntity] { [] }
        func entities(matching string: String) async throws -> [TabEntity] { [] }
    }
}
```

For more information about the `.browser` app intent domain, see [`Browser`](app-schema-domain-browser.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserentity/tab)*
# bookmark

**Framework**: App Intents  
**Kind**: property

The app entity describes a bookmark.

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
var bookmark: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.browser.bookmark` schema:

```swift
@AppEntity(schema: .browser.bookmark)
struct BookmarkEntity: AppEntity {
    static var defaultQuery = Query()

    let id = UUID()

    @Property
    var name: String

    @Property
    var url: URL

    var displayRepresentation: AppIntents.DisplayRepresentation { "Bookmark" }
    struct Query: EntityStringQuery {
        func entities(for identifiers: [BookmarkEntity.ID]) async throws -> [BookmarkEntity] { [] }
        func entities(matching string: String) async throws -> [BookmarkEntity] { [] }
    }
}
```

For more information about the `.browser` app intent domain, see [`Making browser actions available to Siri and Apple Intelligence`](making-browser-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserentity/bookmark)*
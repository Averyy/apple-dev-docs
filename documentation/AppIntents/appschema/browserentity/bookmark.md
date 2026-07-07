# bookmark

**Framework**: App Intents  
**Kind**: property

An entity schema for a bookmark.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var bookmark: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `browser` domain and its content matches the `bookmark` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .browser.bookmark)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `bookmark` schema:

```swift
@AppEntity(schema: .browser.bookmark)
struct BookmarkEntity {
    // MARK: Static

    static let defaultQuery = BookmarkEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var url: URL

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct BookmarkEntityQuery: EntityQuery {
        func entities(for identifiers: [BookmarkEntity.ID]) async throws -> [BookmarkEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var readingListItem: some AppSchemaEntity](appschema/browserentity/readinglistitem.md)
  An entity schema for a reading list item.
- [var tab: some AppSchemaEntity](appschema/browserentity/tab.md)
  An entity schema for a tab.
- [var tabGroup: some AppSchemaEntity](appschema/browserentity/tabgroup.md)
  An entity schema for a tab group.
- [var window: some AppSchemaEntity](appschema/browserentity/window.md)
  An entity schema for a window.
- [AppSchema.BrowserEntity](appschema/browserentity.md)
  Identifies entity schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserentity/bookmark)*
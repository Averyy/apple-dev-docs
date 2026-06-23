# readingListItem

**Framework**: App Intents  
**Kind**: property

An entity schema for a reading list item.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var readingListItem: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `browser` domain and its content matches the `readingListItem` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .browser.readingListItem)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `readingListItem` schema:

```swift
@AppEntity(schema: .browser.readingListItem)
struct ReadingListItemEntity {
    // MARK: Static

    static let defaultQuery = ReadingListItemEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String
    var url: URL

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct ReadingListItemEntityQuery: EntityQuery {
        func entities(for identifiers: [ReadingListItemEntity.ID]) async throws -> [ReadingListItemEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var bookmark: some AppSchemaEntity](appschema/browserentity/bookmark.md)
  An entity schema for a bookmark.
- [var tab: some AppSchemaEntity](appschema/browserentity/tab.md)
  An entity schema for a tab.
- [var tabGroup: some AppSchemaEntity](appschema/browserentity/tabgroup.md)
  An entity schema for a tab group.
- [var window: some AppSchemaEntity](appschema/browserentity/window.md)
  An entity schema for a window.
- [AppSchema.BrowserEntity](appschema/browserentity.md)
  Identifies entity schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserentity/readinglistitem)*
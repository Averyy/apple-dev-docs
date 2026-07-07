# tabGroup

**Framework**: App Intents  
**Kind**: property

An entity schema for a tab group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var tabGroup: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `browser` domain and its content matches the `tabGroup` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .browser.tabGroup)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `tabGroup` schema:

```swift
@AppEntity(schema: .browser.tabGroup)
struct TabGroupEntity {
    // MARK: Static

    static let defaultQuery = TabGroupEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct TabGroupEntityQuery: EntityQuery {
        func entities(for identifiers: [TabGroupEntity.ID]) async throws -> [TabGroupEntity] {
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
- [var readingListItem: some AppSchemaEntity](appschema/browserentity/readinglistitem.md)
  An entity schema for a reading list item.
- [var tab: some AppSchemaEntity](appschema/browserentity/tab.md)
  An entity schema for a tab.
- [var window: some AppSchemaEntity](appschema/browserentity/window.md)
  An entity schema for a window.
- [AppSchema.BrowserEntity](appschema/browserentity.md)
  Identifies entity schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserentity/tabgroup)*
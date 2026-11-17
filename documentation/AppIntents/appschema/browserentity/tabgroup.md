# tabGroup

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a tab group.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var tabGroup: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `browser` domain and its content matches the `tabGroup` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .browser.tabGroup)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `tabGroup` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `browser_tabGroup` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .browser.tabGroup)
struct TabGroupEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more tab group entities, unless you provide another.
    static let defaultQuery = TabGroupEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the tab group entity.
    let id: <#Identifiable.ID#>

    var title: String

    /// The details the system shows to identify the tab group entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more tab group entities by their identifiers.
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

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the tab-group entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Title |

## See Also

### Content and parameter types
- [var bookmark: some AppSchemaEntity](./bookmark.md)
  An entity schema for a bookmark.
- [var readingListItem: some AppSchemaEntity](./readinglistitem.md)
  An entity schema for a reading list item.
- [var tab: some AppSchemaEntity](./tab.md)
  An entity schema for a tab.
- [var window: some AppSchemaEntity](./window.md)
  An entity schema for a window.
- [AppSchema.BrowserEntity](../browserentity.md)
  Identifies entity schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserentity/tabgroup)*
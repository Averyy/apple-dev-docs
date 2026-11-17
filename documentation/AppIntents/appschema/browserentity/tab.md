# tab

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var tab: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `browser` domain and its content matches the `tab` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .browser.tab)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `tab` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `browser_tab` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .browser.tab)
struct TabEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more tab entities, unless you provide another.
    static let defaultQuery = TabEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the tab entity.
    let id: <#Identifiable.ID#>

    var name: String

    var url: URL?

    var isPrivate: Bool

    /// The details the system shows to identify the tab entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more tab entities by their identifiers.
    struct TabEntityQuery: EntityQuery {
        func entities(for identifiers: [TabEntity.ID]) async throws -> [TabEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the tab entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |
| `url` | `URL?` | Foundation | URL |
| `isPrivate` | `Bool` | Swift | Private |

## See Also

### Content and parameter types
- [var bookmark: some AppSchemaEntity](./bookmark.md)
  An entity schema for a bookmark.
- [var readingListItem: some AppSchemaEntity](./readinglistitem.md)
  An entity schema for a reading list item.
- [var tabGroup: some AppSchemaEntity](./tabgroup.md)
  An entity schema for a tab group.
- [var window: some AppSchemaEntity](./window.md)
  An entity schema for a window.
- [AppSchema.BrowserEntity](../browserentity.md)
  Identifies entity schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserentity/tab)*
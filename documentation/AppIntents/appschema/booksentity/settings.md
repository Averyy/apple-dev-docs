# settings

**Framework**: App Intents  
**Kind**: property

An entity schema for  settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var settings: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `books` domain and its content matches the `settings` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .books.settings)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `settings` schema:

```swift
@AppEntity(schema: .books.settings)
struct BookSettingsEntity {
    // MARK: Static

    static let defaultQuery = BookSettingsEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var font: <#BookFont#>
    var fontSize: <#BookFontSize#>
    var theme: <#BookTheme#>
    var pageNavigationSetting: <#BookPageNavigationSetting#>
    var isTextJustified: Bool
    var isAllowMultipleColumns: Bool

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct BookSettingsEntityQuery: EntityQuery {
        func entities(for identifiers: [BookSettingsEntity.ID]) async throws -> [BookSettingsEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var audiobook: some AppSchemaEntity](appschema/booksentity/audiobook.md)
  An entity schema for an audiobook.
- [var book: some AppSchemaEntity](appschema/booksentity/book.md)
  An entity schema for a book.
- [AppSchema.BooksEntity](appschema/booksentity.md)
  Identifies entity schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksentity/settings)*
# settings

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for settings.

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

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `books` domain and its content matches the `settings` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .books.settings)` Swift macro.

The following example shows an app entity that conforms to the `settings` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_settings` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .books.settings)
struct BookSettingsEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more book settings entities, unless you provide another.
    static let defaultQuery = BookSettingsEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the book settings entity.
    let id: <#Identifiable.ID#>

    var font: <#BookFont#>

    var fontSize: <#BookFontSize#>

    var theme: <#BookTheme#>

    var pageNavigationSetting: <#BookPageNavigationSetting#>

    var isTextJustified: Bool

    var isAllowMultipleColumns: Bool

    /// The details the system shows to identify the book settings entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more book settings entities by their identifiers.
    struct BookSettingsEntityQuery: EntityQuery {
        func entities(for identifiers: [BookSettingsEntity.ID]) async throws -> [BookSettingsEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the settings entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `font` | `@AppEnum(schema: .books.font)` | Your app | Font `BookFont` is a placeholder name for a type that conforms to the [`font`](../booksenum/font.md) enum schema, which your app defines and implements. |
| `fontSize` | `@AppEnum(schema: .books.fontSize)` | Your app | Font Size `BookFontSize` is a placeholder name for a type that conforms to the [`fontSize`](../booksenum/fontsize.md) enum schema, which your app defines and implements. |
| `theme` | `@AppEnum(schema: .books.theme)` | Your app | Theme `BookTheme` is a placeholder name for a type that conforms to the [`theme`](../booksenum/theme.md) enum schema, which your app defines and implements. |
| `pageNavigationSetting` | `@AppEnum(schema: .books.pageNavigationSetting)` | Your app | Page Navigation Setting `BookPageNavigationSetting` is a placeholder name for a type that conforms to the [`pageNavigationSetting`](../booksenum/pagenavigationsetting.md) enum schema, which your app defines and implements. |
| `isTextJustified` | `Bool` | Swift | Is Text Justified |
| `isAllowMultipleColumns` | `Bool` | Swift | Is Allow Multiple Columns |

## See Also

### Content and parameter types
- [var audiobook: some AppSchemaEntity](./audiobook.md)
  An entity schema for an audiobook.
- [var book: some AppSchemaEntity](./book.md)
  An entity schema for a book.
- [AppSchema.BooksEntity](../booksentity.md)
  Identifies entity schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksentity/settings)*
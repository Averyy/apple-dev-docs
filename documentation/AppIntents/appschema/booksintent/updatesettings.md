# updateSettings

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that updates the settings for a book.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var updateSettings: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `books` domain and one of your app’s actions matches the `updateSettings` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .books.updateSettings)` Swift macro.

The following example shows an intent that conforms to the `updateSettings` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_updateSettings` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .books.updateSettings)
struct UpdateBookSettingsIntent {
    /// Settings of the book to update.
    var target: <#BookSettingsEntity#>

    /// Font to update to.
    var font: <#BookFont#>?

    /// Theme to update to.
    var theme: <#BookTheme#>?

    /// Navigation style to update to.
    var pageNavigationSetting: <#BookPageNavigationSetting#>?

    /// Whether to justify the text.
    var isTextJustified: Bool?

    /// Whether to allow multiple columns.
    var isAllowMultipleColumns: Bool?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the update-settings intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .books.settings)` | Your app | Settings of the book to update. `BookSettingsEntity` is a placeholder name for a type that conforms to the [`settings`](../booksentity/settings.md) entity schema, which your app defines and implements. |
| `font` | `@AppEnum(schema: .books.font)?` | Your app | Font to update to. `BookFont` is a placeholder name for a type that conforms to the [`font`](../booksenum/font.md) enum schema, which your app defines and implements. |
| `theme` | `@AppEnum(schema: .books.theme)?` | Your app | Theme to update to. `BookTheme` is a placeholder name for a type that conforms to the [`theme`](../booksenum/theme.md) enum schema, which your app defines and implements. |
| `pageNavigationSetting` | `@AppEnum(schema: .books.pageNavigationSetting)?` | Your app | Navigation style to update to. `BookPageNavigationSetting` is a placeholder name for a type that conforms to the [`pageNavigationSetting`](../booksenum/pagenavigationsetting.md) enum schema, which your app defines and implements. |
| `isTextJustified` | `Bool?` | Swift | Whether to justify the text. |
| `isAllowMultipleColumns` | `Bool?` | Swift | Whether to allow multiple columns. |

## See Also

### Actions
- [var navigatePage: some AppSchemaIntent](./navigatepage.md)
  An intent schema that navigates to the next or previous page.
- [var openBook: some AppSchemaIntent](./openbook.md)
  An intent schema that opens the specified book.
- [var updateCharacterSpacing: some AppSchemaIntent](./updatecharacterspacing.md)
  An intent schema that updates the character spacing for a book.
- [var updateFontSize: some AppSchemaIntent](./updatefontsize.md)
  An intent schema that updates the font size for a book.
- [var updateLineSpacing: some AppSchemaIntent](./updatelinespacing.md)
  An intent schema that updates the line spacing for a book.
- [var updateWordSpacing: some AppSchemaIntent](./updatewordspacing.md)
  An intent schema that updates the word spacing for a book.
- [AppSchema.BooksIntent](../booksintent.md)
  Identifies intent schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent/updatesettings)*
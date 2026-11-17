# updateLineSpacing

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that updates the line spacing for a book.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var updateLineSpacing: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `books` domain and one of your app’s actions matches the `updateLineSpacing` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .books.updateLineSpacing)` Swift macro.

The following example shows an intent that conforms to the `updateLineSpacing` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_updateLineSpacing` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .books.updateLineSpacing)
struct UpdateBookLineSpacingIntent {
    /// Settings of the book to update.
    var target: <#BookSettingsEntity#>

    /// Line spacing to update to.
    var changeOperation: <#BookRelativeLineSpacingChange#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the update-line-spacing intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .books.settings)` | Your app | Settings of the book to update. `BookSettingsEntity` is a placeholder name for a type that conforms to the [`settings`](../booksentity/settings.md) entity schema, which your app defines and implements. |
| `changeOperation` | `@AppEnum(schema: .books.relativeLineSpacingChange)` | Your app | Line spacing to update to. `BookRelativeLineSpacingChange` is a placeholder name for a type that conforms to the [`relativeLineSpacingChange`](../booksenum/relativelinespacingchange.md) enum schema, which your app defines and implements. |

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
- [var updateSettings: some AppSchemaIntent](./updatesettings.md)
  An intent schema that updates the settings for a book.
- [var updateWordSpacing: some AppSchemaIntent](./updatewordspacing.md)
  An intent schema that updates the word spacing for a book.
- [AppSchema.BooksIntent](../booksintent.md)
  Identifies intent schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent/updatelinespacing)*
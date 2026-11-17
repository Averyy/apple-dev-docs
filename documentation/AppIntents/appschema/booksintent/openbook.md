# openBook

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens the specified book.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var openBook: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `books` domain and one of your app’s actions matches the `openBook` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .books.openBook)` Swift macro.

The following example shows an intent that conforms to the `openBook` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_openBook` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .books.openBook)
struct OpenBookIntent: OpenIntent {
    /// Book to open.
    var target: <#BookEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the open-book intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .books.book)` | Your app | Book to open. `BookEntity` is a placeholder name for a type that conforms to the [`book`](../booksentity/book.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var navigatePage: some AppSchemaIntent](./navigatepage.md)
  An intent schema that navigates to the next or previous page.
- [var updateCharacterSpacing: some AppSchemaIntent](./updatecharacterspacing.md)
  An intent schema that updates the character spacing for a book.
- [var updateFontSize: some AppSchemaIntent](./updatefontsize.md)
  An intent schema that updates the font size for a book.
- [var updateLineSpacing: some AppSchemaIntent](./updatelinespacing.md)
  An intent schema that updates the line spacing for a book.
- [var updateSettings: some AppSchemaIntent](./updatesettings.md)
  An intent schema that updates the settings for a book.
- [var updateWordSpacing: some AppSchemaIntent](./updatewordspacing.md)
  An intent schema that updates the word spacing for a book.
- [AppSchema.BooksIntent](../booksintent.md)
  Identifies intent schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent/openbook)*
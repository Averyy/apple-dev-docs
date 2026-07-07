# updateCharacterSpacing

**Framework**: App Intents  
**Kind**: property

An intent schema that updates the character spacing for a book.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var updateCharacterSpacing: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `books` domain and one of your app’s actions matches the `updateCharacterSpacing` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .books.updateCharacterSpacing)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateCharacterSpacing` schema:

```swift
@AppIntent(schema: .books.updateCharacterSpacing)
struct UpdateCharacterSpacingIntent {
    var target: <#BookSettingsEntity#>
    var changeOperation: <#BookRelativeCharacterSpacingChange#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var navigatePage: some AppSchemaIntent](appschema/booksintent/navigatepage.md)
  An intent schema that navigates to the next or previous page.
- [var openBook: some AppSchemaIntent](appschema/booksintent/openbook.md)
  An intent schema that opens the specified book.
- [var updateFontSize: some AppSchemaIntent](appschema/booksintent/updatefontsize.md)
  An intent schema that updates the font size for a book.
- [var updateLineSpacing: some AppSchemaIntent](appschema/booksintent/updatelinespacing.md)
  An intent schema that updates the line spacing for a book.
- [var updateSettings: some AppSchemaIntent](appschema/booksintent/updatesettings.md)
  An intent schema that updates the settings for a book.
- [var updateWordSpacing: some AppSchemaIntent](appschema/booksintent/updatewordspacing.md)
  An intent schema that updates the word spacing for a book.
- [AppSchema.BooksIntent](appschema/booksintent.md)
  Identifies intent schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent/updatecharacterspacing)*
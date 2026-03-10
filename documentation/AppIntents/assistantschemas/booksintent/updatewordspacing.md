# updateWordSpacing

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for updating the spacing between words.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var updateWordSpacing: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.books.updateWordSpacing` schema:

```swift
@AppIntent(schema: .books.updateWordSpacing)
struct UpdateWordSpacingIntent: AppIntent {
    @Parameter
    var target: BookSettingsEntity

    @Parameter
    var changeOperation: BookRelativeWordSpacingChange

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var navigatePage: some AssistantSchemas.Intent](assistantschemas/booksintent/navigatepage.md)
  The app intent conforms to the schema for navigating to a specific page of an ebook.
- [var openBook: some AssistantSchemas.Intent](assistantschemas/booksintent/openbook.md)
  The app intent conforms to the schema for opening an ebook.
- [var playAudiobook: some AssistantSchemas.Intent](assistantschemas/booksintent/playaudiobook.md)
  The app intent conforms to the schema for playing an audiobook.
- [var updateCharacterSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatecharacterspacing.md)
  The app intent conforms to the schema for updating the character spacing.
- [var updateFontSize: some AssistantSchemas.Intent](assistantschemas/booksintent/updatefontsize.md)
  The app intent conforms to the schema for updating the font size.
- [var updateLineSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatelinespacing.md)
  The app intent conforms to the schema for updating the line spacing.
- [var updateSettings: some AssistantSchemas.Intent](assistantschemas/booksintent/updatesettings.md)
  The app intent conforms to the schema for updating settings for an ebook.
- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksintent/updatewordspacing)*
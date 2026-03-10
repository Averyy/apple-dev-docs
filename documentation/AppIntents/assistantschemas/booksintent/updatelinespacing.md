# updateLineSpacing

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for updating the line spacing.

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
var updateLineSpacing: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.books.updateLineSpacing` schema:

```swift
@AppIntent(schema: .books.updateLineSpacing)
struct UpdateBookLineSpacingIntent: AppIntent {
    @Parameter
    var target: BookSettingsEntity

    @Parameter
    var changeOperation: BookRelativeLineSpacingChange

    func perform() async throws -> some IntentResult {
        .result()
    }
}
For more information about the `.books` app intent domain,
see <doc:Making-ebook-actions-available-to-siri-and-apple-intelligence>.
For general information about app intent domains, see <doc:Integrating-actions-with-siri-and-apple-intelligence>.
```

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
- [var updateSettings: some AssistantSchemas.Intent](assistantschemas/booksintent/updatesettings.md)
  The app intent conforms to the schema for updating settings for an ebook.
- [var updateWordSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatewordspacing.md)
  The app intent conforms to the schema for updating the spacing between words.
- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksintent/updatelinespacing)*
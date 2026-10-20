# AppSchema.BooksIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the books domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol BooksIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var navigatePage: some AppSchemaIntent](./booksintent/navigatepage.md)
  An intent schema that navigates to the next or previous page.
- [var openBook: some AppSchemaIntent](./booksintent/openbook.md)
  An intent schema that opens the specified book.
- [var playAudiobook: some AppSchemaIntent](./booksintent/playaudiobook.md)
  An intent schema that plays an audiobook.
- [var search: some AppSchemaIntent](./booksintent/search.md)
  An intent schema that opens the app and searches for the given term.
- [var updateCharacterSpacing: some AppSchemaIntent](./booksintent/updatecharacterspacing.md)
  An intent schema that updates the character spacing for a book.
- [var updateFontSize: some AppSchemaIntent](./booksintent/updatefontsize.md)
  An intent schema that updates the font size for a book.
- [var updateLineSpacing: some AppSchemaIntent](./booksintent/updatelinespacing.md)
  An intent schema that updates the line spacing for a book.
- [var updateSettings: some AppSchemaIntent](./booksintent/updatesettings.md)
  An intent schema that updates the settings for a book.
- [var updateWordSpacing: some AppSchemaIntent](./booksintent/updatewordspacing.md)
  An intent schema that updates the word spacing for a book.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var navigatePage: some AppSchemaIntent](./booksintent/navigatepage.md)
  An intent schema that navigates to the next or previous page.
- [var openBook: some AppSchemaIntent](./booksintent/openbook.md)
  An intent schema that opens the specified book.
- [var updateCharacterSpacing: some AppSchemaIntent](./booksintent/updatecharacterspacing.md)
  An intent schema that updates the character spacing for a book.
- [var updateFontSize: some AppSchemaIntent](./booksintent/updatefontsize.md)
  An intent schema that updates the font size for a book.
- [var updateLineSpacing: some AppSchemaIntent](./booksintent/updatelinespacing.md)
  An intent schema that updates the line spacing for a book.
- [var updateSettings: some AppSchemaIntent](./booksintent/updatesettings.md)
  An intent schema that updates the settings for a book.
- [var updateWordSpacing: some AppSchemaIntent](./booksintent/updatewordspacing.md)
  An intent schema that updates the word spacing for a book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent)*
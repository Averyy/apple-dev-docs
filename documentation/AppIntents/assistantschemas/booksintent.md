# AssistantSchemas.BooksIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer ebook and audiobook functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol BooksIntent : AssistantSchemas.Model
```

## Mentions

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var navigatePage: some AssistantSchemas.Intent](assistantschemas/booksintent/navigatepage.md)
  The app intent conforms to the schema for navigating to a specific page of an ebook.
- [var openBook: some AssistantSchemas.Intent](assistantschemas/booksintent/openbook.md)
  The app intent conforms to the schema for opening an ebook.
- [var playAudiobook: some AssistantSchemas.Intent](assistantschemas/booksintent/playaudiobook.md)
  The app intent conforms to the schema for playing an audiobook.
- [var search: some AssistantSchemas.Intent](assistantschemas/booksintent/search.md)
  The app intent conforms to the schema for searching an ebook or audiobook library.
- [var updateCharacterSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatecharacterspacing.md)
  The app intent conforms to the schema for updating the character spacing.
- [var updateFontSize: some AssistantSchemas.Intent](assistantschemas/booksintent/updatefontsize.md)
  The app intent conforms to the schema for updating the font size.
- [var updateLineSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatelinespacing.md)
  The app intent conforms to the schema for updating the line spacing.
- [var updateSettings: some AssistantSchemas.Intent](assistantschemas/booksintent/updatesettings.md)
  The app intent conforms to the schema for updating settings for an ebook.
- [var updateWordSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatewordspacing.md)
  The app intent conforms to the schema for updating the spacing between words.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s ebook and audiobook functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BooksEntity](assistantschemas/booksentity.md)
  Assistant schema conformance for app entities that describe ebooks or audiobooks.
- [AssistantSchemas.BooksEnum](assistantschemas/booksenum.md)
  Assistant schema conformance for types you use to describe ebooks or audiobooks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksintent)*
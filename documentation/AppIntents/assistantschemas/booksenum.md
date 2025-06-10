# AssistantSchemas.BooksEnum

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for types you use to describe ebooks or audiobooks.

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
protocol BooksEnum : AssistantSchemas.Model
```

## Mentions

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var contentType: some AssistantSchemas.Enum](assistantschemas/booksenum/contenttype.md)
  The content type.
- [var font: some AssistantSchemas.Enum](assistantschemas/booksenum/font.md)
  The font for rendering a book.
- [var fontSize: some AssistantSchemas.Enum](assistantschemas/booksenum/fontsize.md)
  The font size for rendering a book.
- [var navigationDirection: some AssistantSchemas.Enum](assistantschemas/booksenum/navigationdirection.md)
  The navigation direction of a book.
- [var pageNavigationSetting: some AssistantSchemas.Enum](assistantschemas/booksenum/pagenavigationsetting.md)
  Navigation settings for rendering a book.
- [var relativeCharacterSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativecharacterspacingchange.md)
  The relative change in character spacing for rendering a book.
- [var relativeFontChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativefontchange.md)
  The relative change of the font for rendering a book.
- [var relativeLineSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativelinespacingchange.md)
  The relative change in line spacing for rendering a book.
- [var relativeWordSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativewordspacingchange.md)
  The relative change in word spacing for rendering a book.
- [var theme: some AssistantSchemas.Enum](assistantschemas/booksenum/theme.md)
  The theme for rendering a book.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EnumSchema](assistantschema/enumschema.md)
- [AssistantSchemas.EnumSchema](assistantschemas/enumschema.md)

## See Also

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s ebook and audiobook functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.
- [AssistantSchemas.BooksEntity](assistantschemas/booksentity.md)
  Assistant schema conformance for app entities that describe ebooks or audiobooks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksenum)*
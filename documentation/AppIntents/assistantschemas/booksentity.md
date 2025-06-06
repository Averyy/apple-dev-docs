# AssistantSchemas.BooksEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe ebooks or audiobooks.

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
protocol BooksEntity : AssistantSchemas.Model
```

## Mentions

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var audiobook: some AssistantSchemas.Entity](assistantschemas/booksentity/audiobook.md)
  The app entity describes an audiobook.
- [var book: some AssistantSchemas.Entity](assistantschemas/booksentity/book.md)
  The app entity describes an ebook.
- [var settings: some AssistantSchemas.Entity](assistantschemas/booksentity/settings.md)
  The app entity describes settings for an audiobook or ebook.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s ebook and audiobook functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.
- [AssistantSchemas.BooksEnum](assistantschemas/booksenum.md)
  Assistant schema conformance for types you use to describe ebooks or audiobooks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksentity)*
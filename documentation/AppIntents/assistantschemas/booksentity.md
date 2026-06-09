# AssistantSchemas.BooksEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe ebooks or audiobooks.

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
protocol BooksEntity : AssistantSchemas.Model
```

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksentity)*
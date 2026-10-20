# AssistantSchemas.Entity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

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
protocol Entity : AssistantSchemas.Model
```

## Topics

### Type Properties
- [static var books: some AssistantSchemas.BooksEntity](./entity/books.md)
  Assistant schema conformance for app entities that describe ebooks or audiobooks.
- [static var browser: some AssistantSchemas.BrowserEntity](./entity/browser.md)
  The app entity describes a data for web browsing functionality.
- [static var files: some AssistantSchemas.FilesEntity](./entity/files.md)
  Assistant schema conformance for app entities that describe file data.
- [static var journal: some AssistantSchemas.JournalEntity](./entity/journal.md)
  Assistant schema conformance for app entities that describe journaling data.
- [static var mail: some AssistantSchemas.MailEntity](./entity/mail.md)
  Assistant schema conformance for app entities that describe email data.
- [static var photos: some AssistantSchemas.PhotosEntity](./entity/photos.md)
  Assistant schema conformance for app entities that describe media assets.
- [static var presentation: some AssistantSchemas.PresentationEntity](./entity/presentation.md)
  Assistant schema conformance for app entities that describe presentation data.
- [static var reader: some AssistantSchemas.ReaderEntity](./entity/reader.md)
  Assistant schema conformance for app entities that describe media assets.
- [static var spreadsheet: some AssistantSchemas.SpreadsheetEntity](./entity/spreadsheet.md)
  Assistant schema conformance for app entities that describe spreadsheet data.
- [static var whiteboard: some AssistantSchemas.WhiteboardEntity](./entity/whiteboard.md)
  Assistant schema conformance for app entities that describe data for whiteboard functionality.
- [static var wordProcessor: some AssistantSchemas.WordProcessorEntity](./entity/wordprocessor.md)
  Assistant schema conformance for app entities that describe text document data.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entity)*
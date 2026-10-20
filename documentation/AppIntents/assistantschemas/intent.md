# AssistantSchemas.Intent

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
protocol Intent : AssistantSchemas.Model
```

## Topics

### Type Properties
- [static var assistant: some AssistantSchemas.AssistantIntent](./intent/assistant.md)
  Assistant schema conformance for types you use for assistant functionality.
- [static var books: some AssistantSchemas.BooksIntent](./intent/books.md)
  Assistant schema conformance for app intents that offer ebook and audiobook viewing and rendering functionality.
- [static var browser: some AssistantSchemas.BrowserIntent](./intent/browser.md)
  Assistant schema conformance for app intents that offer web browsing functionality.
- [static var camera: some AssistantSchemas.CameraIntent](./intent/camera.md)
  Assistant schema conformance for app intents that offer camera functionality.
- [static var files: some AssistantSchemas.FilesIntent](./intent/files.md)
  Assistant schema conformance for app intents that offer file management functionality.
- [static var journal: some AssistantSchemas.JournalIntent](./intent/journal.md)
  Assistant schema conformance for app intents that offer journaling functionality.
- [static var mail: some AssistantSchemas.MailIntent](./intent/mail.md)
  Assistant schema conformance for app intents that offer email functionality.
- [static var photos: some AssistantSchemas.PhotosIntent](./intent/photos.md)
  Assistant schema conformance for app intents that offer photo and video functionality.
- [static var presentation: some AssistantSchemas.PresentationIntent](./intent/presentation.md)
- [static var reader: some AssistantSchemas.ReaderIntent](./intent/reader.md)
  Assistant schema conformance for app intents that offer document viewing and editing functionality.
- [static var spreadsheet: some AssistantSchemas.SpreadsheetIntent](./intent/spreadsheet.md)
  Assistant schema conformance for app intents that offer spreadsheet functionality.
- [static var system: some AssistantSchemas.SystemIntent](./intent/system.md)
  Assistant schema conformance for types you use for system functionality.
- [static var visualIntelligence: some AssistantSchemas.VisualIntelligenceIntent](./intent/visualintelligence.md)
  Assistant schema conformance for app intents that match visual intelligence intents.
- [static var whiteboard: some AssistantSchemas.WhiteboardIntent](./intent/whiteboard.md)
  Assistant schema conformance for app intents that offer whiteboard functionality.
- [static var wordProcessor: some AssistantSchemas.WordProcessorIntent](./intent/wordprocessor.md)
  Assistant schema conformance for app intents that offer word processing functionality.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](../assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](./intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intent)*
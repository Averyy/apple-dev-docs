# App intent domains

**Framework**: Appintents

Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.

#### Overview

To enable enhanced understanding and more conversational interactions with Siri for your app, choose a domain and a schema that match your app’s functionality. By conforming your app intent, app entity, or your app enumeration to a schema, you ensure that Apple Intelligence understands your app’s actions and content. When you’ve identified the schema to use, leverage the [`AssistantIntent(schema:)`](assistantintent(schema:).md), [`AssistantEntity(schema:)`](assistantentity(schema:).md), and [`AssistantEnum(schema:)`](assistantenum(schema:).md) macros to write schema-conforming code.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

To learn more, refer to [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md) and [`Making onscreen content available to Siri and Apple Intelligence`](making-onscreen-content-available-to-siri-and-apple-intelligence.md).

## Topics

### Macros
- [macro AssistantIntent<T>(schema: T)](assistantintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an assistant schema.
- [macro AssistantEntity<T>(schema: T)](assistantentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to an assistant schema.
- [macro AssistantEnum<T>(schema: T)](assistantenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to an assistant schema.
### Books
- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s ebook and audiobook functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.
- [AssistantSchemas.BooksEntity](assistantschemas/booksentity.md)
  Assistant schema conformance for app entities that describe ebooks or audiobooks.
- [AssistantSchemas.BooksEnum](assistantschemas/booksenum.md)
  Assistant schema conformance for types you use to describe ebooks or audiobooks.
### Browser
- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s web browsing functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BrowserIntent](assistantschemas/browserintent.md)
  Assistant schema conformance for app intents that offer web browsing functionality.
- [AssistantSchemas.BrowserEntity](assistantschemas/browserentity.md)
  Assistant schema conformance for app entities that describe data for web browsing functionality.
- [AssistantSchemas.BrowserEnum](assistantschemas/browserenum.md)
  Assistant schema conformance for types you use for web browsing functionality.
### Camera
- [Making camera actions available to Siri and Apple Intelligence](making-camera-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and enumerations to integrate your app’s camera functionality with Siri and Apple Intelligence.
- [AssistantSchemas.CameraIntent](assistantschemas/cameraintent.md)
  Assistant schema conformance for app intents that offer camera functionality.
- [AssistantSchemas.CameraEnum](assistantschemas/cameraenum.md)
  Assistant schema conformance for types you use for camera functionality.
### Document reader
- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s document viewing and editing functionality with Siri and Apple Intelligence.
- [AssistantSchemas.ReaderIntent](assistantschemas/readerintent.md)
  Assistant schema conformance for app intents that offer document viewing and editing functionality.
- [AssistantSchemas.ReaderEntity](assistantschemas/readerentity.md)
  Assistant schema conformance for app entities that describe documents.
- [AssistantSchemas.ReaderEnum](assistantschemas/readerenum.md)
  Assistant schema conformance for types you use to describe documents.
### File management
- [Making file management actions available to Siri and Apple Intelligence](making-file-management-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s file management functionality with Siri and Apple Intelligence.
- [AssistantSchemas.FilesIntent](assistantschemas/filesintent.md)
  Assistant schema conformance for app intents that offer file management functionality.
- [AssistantSchemas.FilesEntity](assistantschemas/filesentity.md)
  Assistant schema conformance for app entities that describe files.
### Journaling
- [Making journaling actions available to Siri and Apple Intelligence](making-journaling-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s journaling functionality with Siri and Apple Intelligence.
- [AssistantSchemas.JournalIntent](assistantschemas/journalintent.md)
  Assistant schema conformance for app intents that offer journaling functionality.
- [AssistantSchemas.JournalEntity](assistantschemas/journalentity.md)
  Assistant schema conformance for app entities that describe journaling data.
### Email
- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s email functionality with Siri and Apple Intelligence.
- [AssistantSchemas.MailIntent](assistantschemas/mailintent.md)
  Assistant schema conformance for app intents that offer email functionality.
- [AssistantSchemas.MailEntity](assistantschemas/mailentity.md)
  Assistant schema conformance for app entities that describe email.
### Photos and videos
- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s photo and video functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PhotosIntent](assistantschemas/photosintent.md)
  Assistant schema conformance for app intents that offer photo and video functionality.
- [AssistantSchemas.PhotosEntity](assistantschemas/photosentity.md)
  Assistant schema conformance for app entities that describe media assets.
- [AssistantSchemas.PhotosEnum](assistantschemas/photosenum.md)
  Assistant schema conformance for types you use to describe photos and videos.
### Presentations
- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s presentation functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PresentationIntent](assistantschemas/presentationintent.md)
  Assistant schema conformance for app intents that offer presentation functionality.
- [AssistantSchemas.PresentationEntity](assistantschemas/presentationentity.md)
  Assistant schema conformance for app entities that describe presentation data.
### Spreadsheets
- [Making spreadsheet actions available to Siri and Apple Intelligence](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s spreadsheet functionality with Siri and Apple Intelligence.
- [AssistantSchemas.SpreadsheetIntent](assistantschemas/spreadsheetintent.md)
  Assistant schema conformance for app intents that offer spreadsheet functionality.
- [AssistantSchemas.SpreadsheetEntity](assistantschemas/spreadsheetentity.md)
  Assistant schema conformance for app entities that describe spreadsheet data.
### System and in-app search
- [Making in-app search actions available to Siri and Apple Intelligence](making-in-app-search-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s search functionality with Siri and Apple Intelligence.
- [AssistantSchemas.SystemIntent](assistantschemas/systemintent.md)
  Assistant schema conformance for app intents that match system-provided intents.
### Whiteboard
- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities that make your app’s whiteboard functionality available to Siri and Apple Intelligence.
- [AssistantSchemas.WhiteboardIntent](assistantschemas/whiteboardintent.md)
  Assistant schema conformance for app intents that offer whiteboard functionality.
- [AssistantSchemas.WhiteboardEntity](assistantschemas/whiteboardentity.md)
  Assistant schema conformance for app entities that describe data for whiteboard functionality.
- [AssistantSchemas.WhiteboardEnum](assistantschemas/whiteboardenum.md)
  Assistant schema conformance for whiteboard types.
### Word processor and text editing
- [Making word processor actions available to Siri and Apple Intelligence](making-word-processor-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities that make your app’s word processor functionality available to Siri and Apple Intelligence.
- [AssistantSchemas.WordProcessorIntent](assistantschemas/wordprocessorintent.md)
  Assistant schema conformance for app intents that offer word processing functionality.
- [AssistantSchemas.WordProcessorEntity](assistantschemas/wordprocessorentity.md)
  Assistant schema conformance for app entities that describe text documents.
### Base protocols
- [Assistant schema base protocols](assistant-schema-base-protocols.md)
  Protocols that provide the underlying functionality for assistant schemas.

## See Also

- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
  Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.
- [Making onscreen content available to Siri and Apple Intelligence](making-onscreen-content-available-to-siri-and-apple-intelligence.md)
  Enable Siri and Apple Intelligence to respond to a person’s questions and action requests for your app’s onscreen content.
- [Making your app’s functionality available to Siri](making-your-app-s-functionality-available-to-siri.md)
  Add assistant schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents/app-intent-domains)*
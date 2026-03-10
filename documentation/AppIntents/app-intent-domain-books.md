# Books

**Framework**: App Intents

App intent schemas you use for ebook reader functionality and content.

## Topics

### Essentials
- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s ebook and audiobook functionality with Siri and Apple Intelligence.
### Actions
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
- [var updateWordSpacing: some AssistantSchemas.Intent](assistantschemas/booksintent/updatewordspacing.md)
  The app intent conforms to the schema for updating the spacing between words.
- [AssistantSchemas.BooksIntent](assistantschemas/booksintent.md)
  Assistant schema conformance for app intents that offer ebook and audiobook functionality.
### Content and parameter types
- [var book: some AssistantSchemas.Entity](assistantschemas/booksentity/book.md)
  The app entity describes an ebook.
- [var audiobook: some AssistantSchemas.Entity](assistantschemas/booksentity/audiobook.md)
  The app entity describes an audiobook.
- [var settings: some AssistantSchemas.Entity](assistantschemas/booksentity/settings.md)
  The app entity describes settings for an audiobook or ebook.
- [AssistantSchemas.BooksEntity](assistantschemas/booksentity.md)
  Assistant schema conformance for app entities that describe ebooks or audiobooks.
### Types for static parameters
- [var contentType: some AssistantSchemas.Enum](assistantschemas/booksenum/contenttype.md)
  The content type.
- [var font: some AssistantSchemas.Enum](assistantschemas/booksenum/font.md)
  The font for rendering a book.
- [var fontSize: some AssistantSchemas.Enum](assistantschemas/booksenum/fontsize.md)
  The font size for rendering a book.
- [var navigationDirection: some AssistantSchemas.Enum](assistantschemas/booksenum/navigationdirection.md)
  The navigation direction of a book.
- [var relativeFontChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativefontchange.md)
  The relative change of the font for rendering a book.
- [var relativeCharacterSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativecharacterspacingchange.md)
  The relative change in character spacing for rendering a book.
- [var relativeLineSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativelinespacingchange.md)
  The relative change in line spacing for rendering a book.
- [var relativeWordSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativewordspacingchange.md)
  The relative change in word spacing for rendering a book.
- [var theme: some AssistantSchemas.Enum](assistantschemas/booksenum/theme.md)
  The theme for rendering a book.
- [var pageNavigationSetting: some AssistantSchemas.Enum](assistantschemas/booksenum/pagenavigationsetting.md)
  Navigation settings for rendering a book.
- [AssistantSchemas.BooksEnum](assistantschemas/booksenum.md)
  Assistant schema conformance for types you use to describe ebooks or audiobooks.
### Deprecated schemas
- [var search: some AssistantSchemas.Intent](assistantschemas/booksintent/search.md)
  The app intent conforms to the schema for searching an ebook or audiobook library.

## See Also

- [Assistant](app-intent-domain-assistant.md)
  An app intent schema that lets people in Japan configure the side button of iPhone to launch your voice-based conversational app.
- [Browser](app-intent-domain-browser.md)
  App intent schemas you use for web browsing functionality and content.
- [Camera](app-intent-domain-camera.md)
  App intent schemas you use for camera functionality and content.
- [File management](app-intent-domain-file-management.md)
  App intent schemas you use for file management functionality and content.
- [Journaling](app-intent-domain-journaling.md)
  App intent schemas you use for journaling functionality and content.
- [Mail](app-intent-domain-mail.md)
  App intent schemas you use for email clients.
- [Photos](app-intent-domain-photos.md)
  App intent schemas you use for photo and video functionality and content.
- [Presentations](app-intent-domain-presentation.md)
  App intent schemas you use for presentation functionality and content.
- [Reader](app-intent-domain-reader.md)
  App intent schemas you use for document reading functionality and content.
- [Spreadsheet](app-intent-domain-spreadsheet.md)
  App intent schemas you use for spreadsheet functionality and content.
- [System and in-app search](app-intent-domain-system-and-search.md)
  App intent schemas you use for in-app search functionality and content.
- [Visual intelligence](app-intent-domain-visual-intelligence.md)
  An app intent schema that lets you integrate your app with visual intelligence.
- [Whiteboard](app-intent-domain-whiteboard.md)
  App intent schemas you use for whiteboard functionality and content.
- [Word proccessor](app-intent-domain-wordprocessor.md)
  App intent schemas you use for text editing functionality and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-intent-domain-books)*
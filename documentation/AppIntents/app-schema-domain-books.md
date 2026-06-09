# Books

**Framework**: App Intents

Make your ebook reader’s actions available in the Shortcuts app by adopting schemas for common reading actions.

#### Overview

The `.books` domain defines app schemas that provide a structured representation for common reading actions and content. Apply schemas in the `.books` domain to make your ebook reader’s functionality available as actions in the Shortcuts app. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `books_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
- [var navigatePage: some AppSchemaIntent](appschema/booksintent/navigatepage.md)
  An intent schema that navigates to the next or previous page.
- [var openBook: some AppSchemaIntent](appschema/booksintent/openbook.md)
  An intent schema that opens the specified book.
- [var updateCharacterSpacing: some AppSchemaIntent](appschema/booksintent/updatecharacterspacing.md)
  An intent schema that updates the character spacing for a book.
- [var updateFontSize: some AppSchemaIntent](appschema/booksintent/updatefontsize.md)
  An intent schema that updates the font size for a book.
- [var updateLineSpacing: some AppSchemaIntent](appschema/booksintent/updatelinespacing.md)
  An intent schema that updates the line spacing for a book.
- [var updateSettings: some AppSchemaIntent](appschema/booksintent/updatesettings.md)
  An intent schema that updates the settings for a book.
- [var updateWordSpacing: some AppSchemaIntent](appschema/booksintent/updatewordspacing.md)
  An intent schema that updates the word spacing for a book.
- [AppSchema.BooksIntent](appschema/booksintent.md)
  Identifies intent schemas in the books domain.
### Content and parameter types
- [var audiobook: some AppSchemaEntity](appschema/booksentity/audiobook.md)
  An entity schema for an audiobook.
- [var book: some AppSchemaEntity](appschema/booksentity/book.md)
  An entity schema for a book.
- [var settings: some AppSchemaEntity](appschema/booksentity/settings.md)
  An entity schema for  settings.
- [AppSchema.BooksEntity](appschema/booksentity.md)
  Identifies entity schemas in the books domain.
### Types for static parameters
- [var contentType: some AppSchemaEnum](appschema/booksenum/contenttype.md)
  An enum schema for a content type parameter.
- [var font: some AppSchemaEnum](appschema/booksenum/font.md)
  An enum schema for a font parameter.
- [var fontSize: some AppSchemaEnum](appschema/booksenum/fontsize.md)
  An enum schema for a font size parameter.
- [var navigationDirection: some AppSchemaEnum](appschema/booksenum/navigationdirection.md)
  An enum schema for a navigation direction parameter.
- [var pageNavigationSetting: some AppSchemaEnum](appschema/booksenum/pagenavigationsetting.md)
  An enum schema for a page navigation setting parameter.
- [var relativeCharacterSpacingChange: some AppSchemaEnum](appschema/booksenum/relativecharacterspacingchange.md)
  An enum schema for a relative character spacing change parameter.
- [var relativeFontChange: some AppSchemaEnum](appschema/booksenum/relativefontchange.md)
  An enum schema for a relative font change parameter.
- [var relativeLineSpacingChange: some AppSchemaEnum](appschema/booksenum/relativelinespacingchange.md)
  An enum schema for a relative line spacing change parameter.
- [var relativeWordSpacingChange: some AppSchemaEnum](appschema/booksenum/relativewordspacingchange.md)
  An enum schema for a relative word spacing change parameter.
- [var theme: some AppSchemaEnum](appschema/booksenum/theme.md)
  An enum schema for a theme parameter.
- [AppSchema.BooksEnum](appschema/booksenum.md)
  Identifies enum schemas in the books domain.
### Deprecated schemas
- [var playAudiobook: some AppSchemaIntent](appschema/booksintent/playaudiobook.md)
  An intent schema that plays an audiobook.
- [var search: some AppSchemaIntent](appschema/booksintent/search.md)
  An intent schema that opens the app and searches for the given term.

## See Also

- [Browser](app-schema-domain-browser.md)
  Make your web browser’s actions available in the Shortcuts app by adopting schemas for common browsing actions.
- [Journaling](app-schema-domain-journaling.md)
  Make your journaling app’s actions available in the Shortcuts app by adopting schemas for journal-entry management.
- [Presentation](app-schema-domain-presentation.md)
  Make your presentation app’s actions available in the Shortcuts app by adopting schemas for common presentation actions.
- [Reader](app-schema-domain-reader.md)
  Make your document reader’s actions available in the Shortcuts app by adopting schemas for document viewing and manipulation.
- [Spreadsheet](app-schema-domain-spreadsheet.md)
  Make your spreadsheet app’s actions available in the Shortcuts app by adopting schemas for spreadsheet management.
- [Whiteboard](app-schema-domain-whiteboard.md)
  Make your whiteboard app’s actions available in the Shortcuts app by adopting schemas for common whiteboard actions.
- [Word processor](app-schema-domain-word-processor.md)
  Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-books)*
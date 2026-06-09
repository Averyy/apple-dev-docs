# Word processor

**Framework**: App Intents

Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.

#### Overview

The `.wordProcessor` domain defines app schemas that provide a structured representation for common document editing actions and content. Apply schemas in the `.wordProcessor` domain to make your word processor’s functionality available as actions in the Shortcuts app. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `wordProcessor_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
- [var addAudioToPage: some AppSchemaIntent](appschema/wordprocessorintent/addaudiotopage.md)
  An intent schema that adds an audio clip to a page.
- [var addImageToPage: some AppSchemaIntent](appschema/wordprocessorintent/addimagetopage.md)
  An intent schema that adds an image to a page.
- [var addTextBoxToPage: some AppSchemaIntent](appschema/wordprocessorintent/addtextboxtopage.md)
  An intent schema that adds a textbox to a page.
- [var addVideoToPage: some AppSchemaIntent](appschema/wordprocessorintent/addvideotopage.md)
  An intent schema that adds a video to a page.
- [var addWebVideoToPage: some AppSchemaIntent](appschema/wordprocessorintent/addwebvideotopage.md)
  An intent schema that adds a web video to a page.
- [var create: some AppSchemaIntent](appschema/wordprocessorintent/create.md)
  An intent schema that opens the app for composing a new text document.
- [var createPage: some AppSchemaIntent](appschema/wordprocessorintent/createpage.md)
  An intent schema that creates a new page in an editor document.
- [var open: some AppSchemaIntent](appschema/wordprocessorintent/open.md)
  An intent schema that opens the app to an editor.
- [var openPage: some AppSchemaIntent](appschema/wordprocessorintent/openpage.md)
  An intent schema that opens an editor document page.
- [AppSchema.WordProcessorIntent](appschema/wordprocessorintent.md)
  Identifies intent schemas in the word processor domain.
### Content and parameter types
- [var document: some AppSchemaEntity](appschema/wordprocessorentity/document.md)
  An entity schema for a document.
- [var page: some AppSchemaEntity](appschema/wordprocessorentity/page.md)
  An entity schema for a page.
- [var template: some AppSchemaEntity](appschema/wordprocessorentity/template.md)
  An entity schema for a template.
- [AppSchema.WordProcessorEntity](appschema/wordprocessorentity.md)
  Identifies entity schemas in the word processor domain.

## See Also

- [Books](app-schema-domain-books.md)
  Make your ebook reader’s actions available in the Shortcuts app by adopting schemas for common reading actions.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-word-processor)*
# Spreadsheet

**Framework**: App Intents

Make your spreadsheet app’s actions available in the Shortcuts app by adopting schemas for spreadsheet management.

#### Overview

The `.spreadsheet` domain defines app schemas that provide a structured representation for common spreadsheet actions and content. Apply schemas in the `.spreadsheet` domain to make your spreadsheet app’s functionality available as actions in the Shortcuts app. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `spreadsheet_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
- [var addAudioToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addaudiotosheet.md)
  An intent schema that adds an audio clip to a sheet.
- [var addCommentToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addcommenttosheet.md)
  An intent schema that adds a comment to a sheet.
- [var addImageToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addimagetosheet.md)
  An intent schema that adds an image to a sheet.
- [var addTextBoxToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addtextboxtosheet.md)
  An intent schema that adds text to a sheet.
- [var addVideoToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addvideotosheet.md)
  An intent schema that adds a video to a sheet.
- [var addWebVideoToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addwebvideotosheet.md)
  An intent schema that adds a web video to a sheet.
- [var create: some AppSchemaIntent](appschema/spreadsheetintent/create.md)
  An intent schema that opens the app for composing a new spreadsheet.
- [var createSheet: some AppSchemaIntent](appschema/spreadsheetintent/createsheet.md)
  An intent schema that creates a new sheet in a spreadsheet.
- [var delete: some AppSchemaIntent](appschema/spreadsheetintent/delete.md)
  An intent schema that deletes existing spreadsheets.
- [var deleteSheet: some AppSchemaIntent](appschema/spreadsheetintent/deletesheet.md)
  An intent schema that deletes sheets in a spreadsheet.
- [var open: some AppSchemaIntent](appschema/spreadsheetintent/open.md)
  An intent schema that opens the app into an existing spreadsheet.
- [var openSheet: some AppSchemaIntent](appschema/spreadsheetintent/opensheet.md)
  An intent schema that opens a sheet.
- [var update: some AppSchemaIntent](appschema/spreadsheetintent/update.md)
  An intent schema that renames an existing spreadsheet.
- [var updateSheet: some AppSchemaIntent](appschema/spreadsheetintent/updatesheet.md)
  An intent schema that updates an existing sheet.
- [AppSchema.SpreadsheetIntent](appschema/spreadsheetintent.md)
  Identifies intent schemas in the spreadsheet domain.
### Content and parameter types
- [var document: some AppSchemaEntity](appschema/spreadsheetentity/document.md)
  An entity schema for a document.
- [var sheet: some AppSchemaEntity](appschema/spreadsheetentity/sheet.md)
  An entity schema for a sheet.
- [var template: some AppSchemaEntity](appschema/spreadsheetentity/template.md)
  An entity schema for a template.
- [AppSchema.SpreadsheetEntity](appschema/spreadsheetentity.md)
  Identifies entity schemas in the spreadsheet domain.

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
- [Whiteboard](app-schema-domain-whiteboard.md)
  Make your whiteboard app’s actions available in the Shortcuts app by adopting schemas for common whiteboard actions.
- [Word processor](app-schema-domain-word-processor.md)
  Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-spreadsheet)*
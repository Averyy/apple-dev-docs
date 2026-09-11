# Files

**Framework**: App Intents

Make your app’s file-management actions available in the Shortcuts app.

#### Overview

The `.files` domain defines app schemas that provide a structured representation for common file-management actions your app can do. Expose your app’s file-management functionality to the system as actions in the Shortcuts app with the schemas in the `.files` domain. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `files_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
- [var createFolder: some AppSchemaIntent](appschema/filesintent/createfolder.md)
  An intent schema that creates a new folder.
- [var deleteFiles: some AppSchemaIntent](appschema/filesintent/deletefiles.md)
  An intent schema that deletes existing files or folders.
- [var moveFiles: some AppSchemaIntent](appschema/filesintent/movefiles.md)
  An intent schema that moves existing files or folders.
- [var openFile: some AppSchemaIntent](appschema/filesintent/openfile.md)
  An intent schema that opens a selected file or folder.
- [var renameFile: some AppSchemaIntent](appschema/filesintent/renamefile.md)
  An intent schema that renames an existing file or folder.
- [AppSchema.FilesIntent](appschema/filesintent.md)
  Identifies intent schemas in the files domain.
### Content and parameter types
- [var file: some AppSchemaEntity](appschema/filesentity/file.md)
  An entity schema for a file.
- [AppSchema.FilesEntity](appschema/filesentity.md)
  Identifies entity schemas in the files domain.

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
- [Word processor](app-schema-domain-word-processor.md)
  Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-files)*
# Files

**Framework**: App Intents

Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.

#### Overview

The `.files` domain defines app schemas that provide a structured representation for common file actions and content. Apply schemas in the `.files` domain to make your app’s file management functionality available to Apple Intelligence and Siri.

The following table maps example phrases that apply to each schema:

| Files intent schemas | Example phrases |
| --- | --- |
| [`renameFile`](appschema/filesintent/renamefile.md) | “Rename this file.” or “Rename document.txt to report.txt.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `files_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

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

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-files)*
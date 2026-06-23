# Notes

**Framework**: App Intents

Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.

#### Overview

The `.notes` domain defines app schemas that provide a structured representation for common note actions and content. Apply schemas in the `.notes` domain to make your app’s note-taking functionality available to Apple Intelligence and Siri.

- **[`createNote`](appschema/notesintent/createnote.md)**: An intent that creates notes when people say phrases like “Create a note called meeting notes.”
- **[`updateNote`](appschema/notesintent/updatenote.md)**: An intent that updates notes when people say phrases like “Rename this note to taxes.” or “Move this note to my work folder.”

> 💡 **Tip**: Xcode generates a template implementation when you type `notes_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var createNote: some AppSchemaIntent](appschema/notesintent/createnote.md)
  An intent schema that creates a new note.
- [var updateNote: some AppSchemaIntent](appschema/notesintent/updatenote.md)
  An intent schema that updates a note.
- [AppSchema.NotesIntent](appschema/notesintent.md)
  Identifies intent schemas in the notes domain.
### Content and parameter types
- [var account: some AppSchemaEntity](appschema/notesentity/account.md)
  An entity schema for an account.
- [var folder: some AppSchemaEntity](appschema/notesentity/folder.md)
  An entity schema for a folder.
- [var note: some AppSchemaEntity](appschema/notesentity/note.md)
  An entity schema for a note.
- [AppSchema.NotesEntity](appschema/notesentity.md)
  Identifies entity schemas in the notes domain.

## See Also

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Files](app-schema-domain-files.md)
  Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-notes)*
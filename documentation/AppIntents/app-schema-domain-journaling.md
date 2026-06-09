# Journaling

**Framework**: App Intents

Make your journaling app’s actions available in the Shortcuts app by adopting schemas for journal-entry management.

#### Overview

The `.journal` domain defines app schemas that provide a structured representation for common journaling actions and content. Apply schemas in the `.journal` domain to make your journaling app’s functionality available as actions in the Shortcuts app. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `journal_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
- [var createAudioEntry: some AppSchemaIntent](appschema/journalintent/createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](appschema/journalintent/createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](appschema/journalintent/deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [var updateEntry: some AppSchemaIntent](appschema/journalintent/updateentry.md)
  An intent schema that updates journal entry.
- [AppSchema.JournalIntent](appschema/journalintent.md)
  Identifies intent schemas in the journal domain.
### Content and parameter types
- [var entry: some AppSchemaEntity](appschema/journalentity/entry.md)
  An entity schema for an entry.
- [AppSchema.JournalEntity](appschema/journalentity.md)
  Identifies entity schemas in the journal domain.
### Deprecated schemas
- [var search: some AppSchemaIntent](appschema/journalintent/search.md)
  An intent schema that searches journal entries.

## See Also

- [Books](app-schema-domain-books.md)
  Make your ebook reader’s actions available in the Shortcuts app by adopting schemas for common reading actions.
- [Browser](app-schema-domain-browser.md)
  Make your web browser’s actions available in the Shortcuts app by adopting schemas for common browsing actions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-journaling)*
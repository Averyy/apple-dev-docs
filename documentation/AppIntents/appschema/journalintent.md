# AppSchema.JournalIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the journal domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol JournalIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createAudioEntry: some AppSchemaIntent](./journalintent/createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](./journalintent/createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](./journalintent/deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [var search: some AppSchemaIntent](./journalintent/search.md)
  An intent schema that searches journal entries.
- [var updateEntry: some AppSchemaIntent](./journalintent/updateentry.md)
  An intent schema that updates journal entry.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var createAudioEntry: some AppSchemaIntent](./journalintent/createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](./journalintent/createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](./journalintent/deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [var updateEntry: some AppSchemaIntent](./journalintent/updateentry.md)
  An intent schema that updates journal entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalintent)*
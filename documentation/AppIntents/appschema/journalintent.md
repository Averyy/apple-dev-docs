# AppSchema.JournalIntent

**Framework**: App Intents  
**Kind**: protocol

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
- [var createAudioEntry: some AppSchemaIntent](appschema/journalintent/createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](appschema/journalintent/createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](appschema/journalintent/deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [var search: some AppSchemaIntent](appschema/journalintent/search.md)
  An intent schema that searches journal entries.
- [var updateEntry: some AppSchemaIntent](appschema/journalintent/updateentry.md)
  An intent schema that updates journal entry.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var createAudioEntry: some AppSchemaIntent](appschema/journalintent/createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](appschema/journalintent/createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](appschema/journalintent/deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [var updateEntry: some AppSchemaIntent](appschema/journalintent/updateentry.md)
  An intent schema that updates journal entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalintent)*
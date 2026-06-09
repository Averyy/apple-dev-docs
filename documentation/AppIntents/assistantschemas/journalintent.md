# AssistantSchemas.JournalIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer journaling functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol JournalIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var createAudioEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/createaudioentry.md)
  The app intent conforms to the schema for creating a voice journal entry.
- [var createEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/createentry.md)
  The app intent conforms to the schema for creating a journal entry.
- [var deleteEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/deleteentry.md)
  The app intent conforms to the schema for deleting a journal entry.
- [var search: some AssistantSchemas.Intent](assistantschemas/journalintent/search.md)
  The app intent conforms to the schema for searching in journal entries.
- [var updateEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/updateentry.md)
  The app intent conforms to the schema for updating a journal entry.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/journalintent)*
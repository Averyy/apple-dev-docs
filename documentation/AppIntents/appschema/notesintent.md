# AppSchema.NotesIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the notes domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol NotesIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var appendText: some AppSchemaIntent](./notesintent/appendtext.md)
  An intent schema that adds text to the end of an existing note.
- [var createNote: some AppSchemaIntent](./notesintent/createnote.md)
  An intent schema that creates a new note.
- [var updateNote: some AppSchemaIntent](./notesintent/updatenote.md)
  An intent schema that updates a note.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var createNote: some AppSchemaIntent](./notesintent/createnote.md)
  An intent schema that creates a new note.
- [var updateNote: some AppSchemaIntent](./notesintent/updatenote.md)
  An intent schema that updates a note.
- [var appendText: some AppSchemaIntent](./notesintent/appendtext.md)
  An intent schema that adds text to the end of an existing note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesintent)*
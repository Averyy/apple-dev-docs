# AppSchema.NotesIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the notes domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol NotesIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createNote: some AppSchemaIntent](appschema/notesintent/createnote.md)
  An intent schema that creates a new note.
- [var updateNote: some AppSchemaIntent](appschema/notesintent/updatenote.md)
  An intent schema that updates a note.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var createNote: some AppSchemaIntent](appschema/notesintent/createnote.md)
  An intent schema that creates a new note.
- [var updateNote: some AppSchemaIntent](appschema/notesintent/updatenote.md)
  An intent schema that updates a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesintent)*
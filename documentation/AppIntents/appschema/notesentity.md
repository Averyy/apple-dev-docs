# AppSchema.NotesEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the notes domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol NotesEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var account: some AppSchemaEntity](./notesentity/account.md)
  An entity schema for an account.
- [var folder: some AppSchemaEntity](./notesentity/folder.md)
  An entity schema for a folder.
- [var note: some AppSchemaEntity](./notesentity/note.md)
  An entity schema for a note.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var account: some AppSchemaEntity](./notesentity/account.md)
  An entity schema for an account.
- [var folder: some AppSchemaEntity](./notesentity/folder.md)
  An entity schema for a folder.
- [var note: some AppSchemaEntity](./notesentity/note.md)
  An entity schema for a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesentity)*
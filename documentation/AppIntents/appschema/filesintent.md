# AppSchema.FilesIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the files domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol FilesIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createFolder: some AppSchemaIntent](./filesintent/createfolder.md)
  An intent schema that creates a new folder.
- [var deleteFiles: some AppSchemaIntent](./filesintent/deletefiles.md)
  An intent schema that deletes existing files or folders.
- [var moveFiles: some AppSchemaIntent](./filesintent/movefiles.md)
  An intent schema that moves existing files or folders.
- [var openFile: some AppSchemaIntent](./filesintent/openfile.md)
  An intent schema that opens a selected file or folder.
- [var renameFile: some AppSchemaIntent](./filesintent/renamefile.md)
  An intent schema that renames an existing file or folder.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var createFolder: some AppSchemaIntent](./filesintent/createfolder.md)
  An intent schema that creates a new folder.
- [var deleteFiles: some AppSchemaIntent](./filesintent/deletefiles.md)
  An intent schema that deletes existing files or folders.
- [var moveFiles: some AppSchemaIntent](./filesintent/movefiles.md)
  An intent schema that moves existing files or folders.
- [var openFile: some AppSchemaIntent](./filesintent/openfile.md)
  An intent schema that opens a selected file or folder.
- [var renameFile: some AppSchemaIntent](./filesintent/renamefile.md)
  An intent schema that renames an existing file or folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/filesintent)*
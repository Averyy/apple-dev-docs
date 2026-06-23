# AppSchema.FilesIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the files domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol FilesIntent : AppSchema.Kind
```

## Topics

### Instance Properties
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

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/filesintent)*
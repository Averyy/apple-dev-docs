# AssistantSchemas.FilesIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app intents that offer file management functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol FilesIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var createFolder: some AssistantSchemas.Intent](./filesintent/createfolder.md)
  The app intent conforms to the schema for creating a folder.
- [var deleteFiles: some AssistantSchemas.Intent](./filesintent/deletefiles.md)
  The app intent conforms to the schema for deleting files.
- [var moveFiles: some AssistantSchemas.Intent](./filesintent/movefiles.md)
  The app intent conforms to the schema for moving a file.
- [var openFile: some AssistantSchemas.Intent](./filesintent/openfile.md)
  The app intent conforms to the schema for opening a file.
- [var renameFile: some AssistantSchemas.Intent](./filesintent/renamefile.md)
  The app intent conforms to the schema for renaming a file.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](../assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](./intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/filesintent)*
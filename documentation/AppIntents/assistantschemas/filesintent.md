# AssistantSchemas.FilesIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer file management functionality.

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
protocol FilesIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var createFolder: some AssistantSchemas.Intent](assistantschemas/filesintent/createfolder.md)
  The app intent conforms to the schema for creating a folder.
- [var deleteFiles: some AssistantSchemas.Intent](assistantschemas/filesintent/deletefiles.md)
  The app intent conforms to the schema for deleting files.
- [var moveFiles: some AssistantSchemas.Intent](assistantschemas/filesintent/movefiles.md)
  The app intent conforms to the schema for moving a file.
- [var openFile: some AssistantSchemas.Intent](assistantschemas/filesintent/openfile.md)
  The app intent conforms to the schema for opening a file.
- [var renameFile: some AssistantSchemas.Intent](assistantschemas/filesintent/renamefile.md)
  The app intent conforms to the schema for renaming a file.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/filesintent)*
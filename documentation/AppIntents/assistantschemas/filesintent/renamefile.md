# renameFile

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for renaming a file.

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
var renameFile: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.files.renameFile` schema:

```swift
@AppIntent(schema: .files.renameFile)
struct RenameFileIntent: AppIntent {
    @Parameter
    var target: ExampleFileEntity

    @Parameter
    var newName: String?

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.files` app intent domain, see [`Making file management actions available to Siri and Apple Intelligence`](making-file-management-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var createFolder: some AssistantSchemas.Intent](assistantschemas/filesintent/createfolder.md)
  The app intent conforms to the schema for creating a folder.
- [var deleteFiles: some AssistantSchemas.Intent](assistantschemas/filesintent/deletefiles.md)
  The app intent conforms to the schema for deleting files.
- [var moveFiles: some AssistantSchemas.Intent](assistantschemas/filesintent/movefiles.md)
  The app intent conforms to the schema for moving a file.
- [var openFile: some AssistantSchemas.Intent](assistantschemas/filesintent/openfile.md)
  The app intent conforms to the schema for opening a file.
- [AssistantSchemas.FilesIntent](assistantschemas/filesintent.md)
  Assistant schema conformance for app intents that offer file management functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/filesintent/renamefile)*
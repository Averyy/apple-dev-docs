# openFile

**Framework**: App Intents  
**Kind**: property

An intent schema that opens a selected file or folder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var openFile: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `files` domain and one of your app’s actions matches the `openFile` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .files.openFile)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `openFile` schema:

```swift
@AppIntent(schema: .files.openFile)
struct OpenFileIntent: OpenIntent {
    var target: <#FileEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createFolder: some AppSchemaIntent](appschema/filesintent/createfolder.md)
  An intent schema that creates a new folder.
- [var deleteFiles: some AppSchemaIntent](appschema/filesintent/deletefiles.md)
  An intent schema that deletes existing files or folders.
- [var moveFiles: some AppSchemaIntent](appschema/filesintent/movefiles.md)
  An intent schema that moves existing files or folders.
- [var renameFile: some AppSchemaIntent](appschema/filesintent/renamefile.md)
  An intent schema that renames an existing file or folder.
- [AppSchema.FilesIntent](appschema/filesintent.md)
  Identifies intent schemas in the files domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/filesintent/openfile)*
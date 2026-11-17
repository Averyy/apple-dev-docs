# openFile

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens a selected file or folder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var openFile: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `files` domain and one of your app’s actions matches the `openFile` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .files.openFile)` Swift macro.

The following example shows an intent that conforms to the `openFile` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `files_openFile` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .files.openFile)
struct OpenFileIntent: OpenIntent {
    /// File or folder to open in the owning app.
    var target: <#FileEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the open-file intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .files.file)` | Your app | File or folder to open in the owning app. `FileEntity` is a placeholder name for a type that conforms to the [`file`](../filesentity/file.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createFolder: some AppSchemaIntent](./createfolder.md)
  An intent schema that creates a new folder.
- [var deleteFiles: some AppSchemaIntent](./deletefiles.md)
  An intent schema that deletes existing files or folders.
- [var moveFiles: some AppSchemaIntent](./movefiles.md)
  An intent schema that moves existing files or folders.
- [var renameFile: some AppSchemaIntent](./renamefile.md)
  An intent schema that renames an existing file or folder.
- [AppSchema.FilesIntent](../filesintent.md)
  Identifies intent schemas in the files domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/filesintent/openfile)*
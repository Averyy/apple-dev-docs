# Making file management actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s file management functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s file management functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app entity implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows a person to open a file, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.files` domain and the [`openFile`](assistantschemas/filesintent/openfile.md) schema:

```swift
@AssistantIntent(schema: .files.openFile)
struct OpenFileIntent: OpenIntent {
    var target: FileEntity

   func perform() async throws -> some IntentResult {
        return .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.files` domain, see [`AssistantSchemas.FilesIntent`](assistantschemas/filesintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `FileEntity`. The following code snippet shows how the `FileEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AssistantEntity(schema: .files.file)
struct FilesEntity: FileEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [FilesEntity.ID]) async throws -> [FilesEntity] { [] }
        func entities(matching string: String) async throws -> [FilesEntity] { [] }
    }
    static var defaultQuery = Query()

    static var supportedContentTypes = [UTType.image]
    var displayRepresentation: AppIntents.DisplayRepresentation { "Provide a display representation." }

    var id: FileEntityIdentifier

    var creationDate: Date?
    var fileModificationDate: Date?
}
```

The assistant schema for the `FileEntity` consists of the `.files` domain and the [`file`](assistantschemas/filesentity/file.md) schema.

For a list of available app entity schemas in the `.files` domain, see [`AssistantSchemas.FilesEntity`](assistantschemas/filesentity.md).

## See Also

- [AssistantSchemas.FilesIntent](assistantschemas/filesintent.md)
  Assistant schema conformance for app intents that offer file management functionality.
- [AssistantSchemas.FilesEntity](assistantschemas/filesentity.md)
  Assistant schema conformance for app entities that describe files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-file-management-actions-available-to-siri-and-apple-intelligence)*
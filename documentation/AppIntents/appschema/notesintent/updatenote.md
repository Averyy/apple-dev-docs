# updateNote

**Framework**: App Intents  
**Kind**: property

An intent schema that updates a note.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var updateNote: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `notes` domain and one of your app’s actions matches the `updateNote` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .notes.updateNote)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateNote` schema:

```swift
@AppIntent(schema: .notes.updateNote)
struct UpdateNoteIntent {
    var target: <#NoteEntity#>
    var name: String?
    var attachments: [IntentFile]?
    var tags: [<#TagEntity#>]?
    var isPinned: Bool?
    var folder: <#FolderEntity#>?

    func perform() async throws -> some ReturnsValue<<#NoteEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createNote: some AppSchemaIntent](appschema/notesintent/createnote.md)
  An intent schema that creates a new note.
- [AppSchema.NotesIntent](appschema/notesintent.md)
  Identifies intent schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesintent/updatenote)*
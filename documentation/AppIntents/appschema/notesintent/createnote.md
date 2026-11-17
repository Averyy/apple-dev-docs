# createNote

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that creates a new note.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var createNote: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `notes` domain and one of your app’s actions matches the `createNote` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .notes.createNote)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createNote` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `notes_createNote` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .notes.createNote)
struct CreateNoteIntent {
    /// Title of the new note.
    var name: AttributedString

    /// The content of the new note.
    var content: AttributedString?

    /// Attachments to add to the new note.
    var attachments: [IntentFile]

    /// Whether the new note is pinned to the top of the person's list of notes.
    var isPinned: Bool

    /// Folder in which to create the new note.
    var folder: <#FolderEntity#>?

    func perform() async throws -> some ReturnsValue<<#NoteEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create-note intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `AttributedString` | Foundation | Title of the new note. |
| `content` | `AttributedString?` | Foundation | The content of the new note. |
| `attachments` | `[IntentFile]` | App Intents | Attachments to add to the new note. |
| `isPinned` | `Bool` | Swift | Whether the new note is pinned to the top of the person’s list of notes. |
| `folder` | `@AppEntity(schema: .notes.folder)?` | Your app | Folder in which to create the new note. `FolderEntity` is a placeholder name for a type that conforms to the [`folder`](../notesentity/folder.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var updateNote: some AppSchemaIntent](./updatenote.md)
  An intent schema that updates a note.
- [var appendText: some AppSchemaIntent](./appendtext.md)
  An intent schema that adds text to the end of an existing note.
- [AppSchema.NotesIntent](../notesintent.md)
  Identifies intent schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesintent/createnote)*
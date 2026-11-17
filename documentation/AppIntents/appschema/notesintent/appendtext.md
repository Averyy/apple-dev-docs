# appendText

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that adds text to the end of an existing note.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var appendText: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `notes` domain and one of your app’s actions matches the `appendText` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .notes.appendText)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `appendText` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `notes_appendText` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .notes.appendText)
struct NoteAppendTextIntent {
    /// The text context to append.
    var content: AttributedString

    /// The note to edit.
    var target: <#NoteEntity#>

    func perform() async throws -> some ReturnsValue<<#NoteEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the append-text intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `content` | `AttributedString` | Foundation | The text context to append. |
| `target` | `@AppEntity(schema: .notes.note)` | Your app | The note to edit. `NoteEntity` is a placeholder name for a type that conforms to the [`note`](../notesentity/note.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createNote: some AppSchemaIntent](./createnote.md)
  An intent schema that creates a new note.
- [var updateNote: some AppSchemaIntent](./updatenote.md)
  An intent schema that updates a note.
- [AppSchema.NotesIntent](../notesintent.md)
  Identifies intent schemas in the notes domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/notesintent/appendtext)*
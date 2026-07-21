# WritableDocument

**Framework**: SwiftUI  
**Kind**: protocol

A document type that supports writing to file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol WritableDocument : AnyObject
```

#### Overview

Conform to `WritableDocument` to add save and export capabilities. Most documents also conform to [`ReadableDocument`](readabledocument.md) — use the [`Document`](document.md) protocol as a shorthand for both.

The document saving has three steps:

1. SwiftUI calls [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md) on the main actor.
2. SwiftUI calls [`writer(configuration:)`](writabledocument/writer(configuration:).md) to get a writer.
3. The writer’s `DocumentWriter/write(content:to:previous:progress:)` runs in the background with coordinated file access.

> ❗ **Important**: Without registered undo actions, SwiftUI won’t trigger autosave. Register undo actions with the undo manager from the `View` environment for every user-facing change.

Example using [`FileWrapperDocumentWriter`](filewrapperdocumentwriter.md):

```swift
@Observable
final class NoteDocument: WritableDocument {
    static let writableContentTypes: [UTType] = [.markdown]

    var text = ""

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(
                regularFileWithContents: Data(snapshot.utf8)
            )
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String { text }
}
```

Register undo actions in the view using the environment’s `UndoManager`. This ensures SwiftUI detects unsaved changes and triggers autosave:

```swift
struct NoteEditorView: View {
    @Bindable var document: NoteDocument
    @Environment(\.undoManager) private var undoManager

    var body: some View {
        TextEditor(text: $document.text)
            .onChange(of: document.text) { oldValue, _ in
                undoManager?.registerUndo(
                    withTarget: document
                ) { document in
                    document.text = oldValue
                }
            }
    }
}
```

## Topics

### Writing a document
- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The content types this document can save or export to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a writer to save this document to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Captures the document’s current state for saving.

## Relationships

### Inherited By
- [Document](document.md)

## See Also

- [protocol Document](document.md)
  A document that supports both reading and writing.
- [protocol ReadableDocument](readabledocument.md)
  A document type that supports reading from file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  The configuration of an open document that stores its file URL, last modification date, and related metadata.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Context about how a document was created.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument)*
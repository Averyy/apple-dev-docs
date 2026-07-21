# Document

**Framework**: SwiftUI  
**Kind**: protocol

A document that supports both reading and writing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Document : ReadableDocument, WritableDocument
```

#### Overview

`Document` is a convenience protocol that combines [`ReadableDocument`](readabledocument.md) and [`WritableDocument`](writabledocument.md). Conform to it when your document can both open and save files:

```swift
@Observable
final class TextDocument: Document {
    static let readableContentTypes = [UTType.plainText]

    var text: String = ""

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            guard let data =
                fileWrapper.regularFileContents else {
                throw CocoaError(.fileReadCorruptFile)
            }
            return String(decoding: data, as: UTF8.self)
        }
    }

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(
                regularFileWithContents: Data(snapshot.utf8)
            )
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String { text }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        text = snapshot
    }
}
```

Use [`DocumentGroup`](documentgroup.md) as your app’s first scene to opt into the document infrastructure (autosaving, file coordination, undo management, conflict resolution):

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup { document in
            TextEditorView(document: document)
        } makeDocument: { configuration, context in
            TextDocument()
        }
    }
}
```

For a read-only document, conform only to [`ReadableDocument`](readabledocument.md).

The document can be `@MainActor` or nonisolated, `Sendable` or not — use whichever works best for the app.

## Relationships

### Inherits From
- [ReadableDocument](readabledocument.md)
- [WritableDocument](writabledocument.md)

## See Also

- [protocol ReadableDocument](readabledocument.md)
  A document type that supports reading from file.
- [protocol WritableDocument](writabledocument.md)
  A document type that supports writing to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  The configuration of an open document that stores its file URL, last modification date, and related metadata.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Context about how a document was created.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/document)*
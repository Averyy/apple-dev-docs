# init(viewer:makeReadableDocument:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a document group capable of opening and viewing read-only documents.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder viewer: @escaping (Document) -> Content, makeReadableDocument: @escaping @MainActor (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)
```

Available when `Document` conforms to `Observable`, `Document` conforms to `ReadableDocument`, `Content` conforms to `View`, and `Document.Reader.Source` is `URL`.

## Parameters

- `viewer`: The viewing UI for the provided document.
- `makeReadableDocument`: A closure that creates the document instance. Throw `CancellationError` to indicate that document opening was cancelled.

## See Also

### Creating a document group
- [init(allowCreating: Bool, editor: (Document) -> Content, makeDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](./init%28allowcreating,editor,makedocument%29.md)
  Creates a document group capable of creating, viewing, and editing documents.
- [init(newDocument:editor:)](./init%28newdocument,editor%29.md)
  Creates a document group for creating and editing file documents.
- [init(viewing:viewer:)](./init%28viewing,viewer%29.md)
  Creates a document group capable of viewing file documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewer:makereadabledocument:))*
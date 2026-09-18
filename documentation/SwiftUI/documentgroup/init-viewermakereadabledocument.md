# init(viewer:makeReadableDocument:)

**Framework**: SwiftUI  
**Kind**: init

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

## Parameters

- `viewer`: The viewing UI for the provided document.
- `makeReadableDocument`: A closure that creates the document instance. Throw `CancellationError` to indicate that document opening was cancelled.

## See Also

- [init(allowCreating: Bool, editor: (Document) -> Content, makeDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](documentgroup/init(allowcreating:editor:makedocument:).md)
  Creates a document group capable of creating, viewing, and editing documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewer:makereadabledocument:))*
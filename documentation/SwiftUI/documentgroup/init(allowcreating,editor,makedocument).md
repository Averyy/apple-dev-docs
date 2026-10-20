# init(allowCreating:editor:makeDocument:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a document group capable of creating, viewing, and editing documents.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
init(allowCreating: Bool = true, @ContentBuilder editor: @escaping (Document) -> Content, makeDocument: @escaping @MainActor (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)
```

Available when `Document` conforms to `Observable`, `Document` conforms to `Document`, `Content` conforms to `View`, `Document.Reader.Source` is `URL`, and `Document.Writer.Destination` is `URL`.

## Parameters

- `allowCreating`: Whether the document group supports creating new documents in addition to opening and editing existing ones.
- `editor`: The editing UI for the provided document.
- `makeDocument`: A closure that creates the document instance. Throw `CancellationError` to indicate that document creation was cancelled.

## See Also

### Creating a document group
- [init(viewer: (Document) -> Content, makeReadableDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](./init%28viewer,makereadabledocument%29.md)
  Creates a document group capable of opening and viewing read-only documents.
- [init(newDocument:editor:)](./init%28newdocument,editor%29.md)
  Creates a document group for creating and editing file documents.
- [init(viewing:viewer:)](./init%28viewing,viewer%29.md)
  Creates a document group capable of viewing file documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(allowcreating:editor:makedocument:))*
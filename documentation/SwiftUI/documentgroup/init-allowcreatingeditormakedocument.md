# init(allowCreating:editor:makeDocument:)

**Framework**: SwiftUI  
**Kind**: init

Creates a document group capable of creating, viewing, and editing documents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(allowCreating: Bool = true, @ContentBuilder editor: @escaping (Document) -> Content, makeDocument: @escaping (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)
```

## Parameters

- `allowCreating`: Whether the document group supports creating new documents in addition to opening and editing existing ones.
- `editor`: The editing UI for the provided document.
- `makeDocument`: A closure that creates the document instance. Throw `CancellationError` to indicate that document creation was cancelled.

## See Also

- [init(newDocument:editor:)](documentgroup/init(newdocument:editor:).md)
  Creates a document group for creating and editing file documents.
- [init(viewing:viewer:)](documentgroup/init(viewing:viewer:).md)
  Creates a document group capable of viewing file documents.
- [init(viewer: (Document) -> Content, makeReadableDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](documentgroup/init(viewer:makereadabledocument:).md)
  Creates a document group capable of opening and viewing read-only documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(allowcreating:editor:makedocument:))*
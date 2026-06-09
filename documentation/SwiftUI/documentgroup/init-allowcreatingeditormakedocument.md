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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(allowcreating:editor:makedocument:))*
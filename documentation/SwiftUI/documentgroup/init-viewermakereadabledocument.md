# init(viewer:makeReadableDocument:)

**Framework**: SwiftUI  
**Kind**: init

Creates a document group capable of opening and viewing read-only documents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(@ContentBuilder viewer: @escaping (Document) -> Content, makeReadableDocument: @escaping (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)
```

## Parameters

- `viewer`: The viewing UI for the provided document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewer:makereadabledocument:))*
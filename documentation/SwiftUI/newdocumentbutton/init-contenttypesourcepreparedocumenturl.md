# init(_:contentType:source:prepareDocumentURL:)

**Framework**: SwiftUI  
**Kind**: init

Creates and opens new URL-based documents from a template picker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(_ title: LocalizedStringKey, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

## Parameters

- `title`: A title key for the button.
- `contentType`: The content type of the document to create.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](filedocumentconfiguration.md) or [`URLDocumentConfiguration`](urldocumentconfiguration.md).
- `prepareDocumentURL`: Called when the user taps the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:preparedocumenturl:))*
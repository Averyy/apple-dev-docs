# init(_:contentType:source:_:)

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
init(_ label: Text? = nil, contentType: UTType, source: DocumentCreationSource, _ prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

#### Discussion

```swift
NewDocumentButton(
    contentType: .text,
    source: .template
) {
    try await withCheckedThrowingContinuation { continuation in
        documentCreationContinuation = continuation
        showTemplatePicker = true
    }
}
```

## Parameters

- `label`: A label for the button.
- `contentType`: The content type of the document to create.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](filedocumentconfiguration.md) or [`URLDocumentConfiguration`](urldocumentconfiguration.md).
- `prepareDocumentURL`: Called when the user taps the button. Present a template picker or other UI, then return the URL of the prepared document, `nil` to request an empty document, or throw on cancellation.

## See Also

- [init(_:contentType:source:)](newdocumentbutton/init(_:contenttype:source:).md)
  Creates and opens new documents, tagging them with a creation source.
- [init(_:contentType:source:prepareDocumentURL:)](newdocumentbutton/init(_:contenttype:source:preparedocumenturl:).md)
  Creates and opens new URL-based documents from a template picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:_:))*
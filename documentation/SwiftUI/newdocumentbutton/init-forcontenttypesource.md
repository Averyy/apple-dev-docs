# init(_:for:contentType:source:_:)

**Framework**: SwiftUI  
**Kind**: init

Creates and opens new documents from a template picker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init<D>(_ label: Text? = nil, for documentType: D.Type = D.self, contentType: UTType? = nil, source: DocumentCreationSource, _ prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

#### Discussion

```swift
NewDocumentButton(
    Text("New from template"),
    for: TextDocument.self,
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
- `documentType`: The type of document to create.
- `contentType`: An optional content type of the document to create.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](filedocumentconfiguration.md) or [`URLDocumentConfiguration`](urldocumentconfiguration.md).
- `prepareDocument`: Called when the user taps the button. Present a template picker or other UI, then return the prepared document, `nil` to request an empty document, or throw on cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:source:_:))*
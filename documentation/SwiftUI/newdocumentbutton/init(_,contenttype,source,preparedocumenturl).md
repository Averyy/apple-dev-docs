# init(_:contentType:source:prepareDocumentURL:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates and opens new URL-based documents from a template picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
init(_ title: LocalizedStringKey, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ title: LocalizedStringResource, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

```swift
nonisolated
init(_ title: some StringProtocol, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

## Parameters

- `title`: A title key for the button.
- `contentType`: The content type of the document to create.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](../filedocumentconfiguration.md) or [`URLDocumentConfiguration`](../urldocumentconfiguration.md).
- `prepareDocumentURL`: Called when the user taps the button.

## See Also

### Creating and opening a document with a creation source
- [init(_:contentType:source:)](./init%28_,contenttype,source%29.md)
  Creates and opens new documents, tagging them with a creation source.
- [init(Text?, contentType: UTType, source: DocumentCreationSource, () async throws -> URL?)](./init%28_,contenttype,source,_%29.md)
  Creates and opens new URL-based documents from a template picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:preparedocumenturl:))*
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
init(_ title: LocalizedStringResource, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ title: LocalizedStringKey, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

```swift
nonisolated
init(_ title: some StringProtocol, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

## Parameters

- `title`: A localized string resource for the button.
- `contentType`: The content type of the document to create.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](../filedocumentconfiguration.md) or [`URLDocumentConfiguration`](../urldocumentconfiguration.md).
- `prepareDocumentURL`: Called when the user taps the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:preparedocumenturl:)-5u6fl)*
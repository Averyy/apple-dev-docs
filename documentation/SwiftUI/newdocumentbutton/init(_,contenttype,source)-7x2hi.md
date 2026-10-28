# init(_:contentType:source:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates and opens new documents, tagging them with a creation source.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
init(_ title: some StringProtocol, contentType: UTType? = nil, source: DocumentCreationSource)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ label: Text? = nil, contentType: UTType? = nil, source: DocumentCreationSource)
```

```swift
nonisolated
init(_ title: LocalizedStringKey, contentType: UTType? = nil, source: DocumentCreationSource)
```

```swift
nonisolated
init(_ title: LocalizedStringResource, contentType: UTType? = nil, source: DocumentCreationSource)
```

## Parameters

- `title`: A title string to use as the button title.
- `contentType`: An optional content type of the document to create.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](../filedocumentconfiguration.md) or [`URLDocumentConfiguration`](../urldocumentconfiguration.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:)-7x2hi)*
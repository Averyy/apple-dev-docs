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
init(_ label: Text? = nil, contentType: UTType? = nil, source: DocumentCreationSource)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ title: LocalizedStringKey, contentType: UTType? = nil, source: DocumentCreationSource)
```

```swift
nonisolated
init(_ title: LocalizedStringResource, contentType: UTType? = nil, source: DocumentCreationSource)
```

```swift
nonisolated
init(_ title: some StringProtocol, contentType: UTType? = nil, source: DocumentCreationSource)
```

#### Discussion

```swift
extension DocumentCreationSource {
    static let brainstorming: Self =
        DocumentCreationSource(id: "brainstorming")
}

DocumentGroupLaunchScene("Meeting Minutes") {
    NewDocumentButton(Text("New meeting minutes…"))
    NewDocumentButton(
        Text("New brainstorming meeting…"),
        source: .brainstorming
    )
}
```

## Parameters

- `label`: A label for the button.
- `contentType`: An optional content type of the document to create. If not provided, the first content type of the first document type listed in the app definition is used.
- `source`: A source for the document creation flow. When a document is created, you can retrieve its source from [`FileDocumentConfiguration`](../filedocumentconfiguration.md) or [`URLDocumentConfiguration`](../urldocumentconfiguration.md).

## See Also

### Creating and opening a document with a creation source
- [init(Text?, contentType: UTType, source: DocumentCreationSource, () async throws -> URL?)](./init%28_,contenttype,source,_%29.md)
  Creates and opens new URL-based documents from a template picker.
- [init(_:contentType:source:prepareDocumentURL:)](./init%28_,contenttype,source,preparedocumenturl%29.md)
  Creates and opens new URL-based documents from a template picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:))*
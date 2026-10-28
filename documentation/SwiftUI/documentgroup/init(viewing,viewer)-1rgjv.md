# init(viewing:viewer:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a document group that is able to view reference file documents.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Create a DocumentGroup with an object conforming to Document protocol instead.

## Declaration

```swift
nonisolated
init(viewing documentType: Document.Type, @ContentBuilder viewer: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content)
```

Available when `Document` conforms to `ReferenceFileDocument` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(viewing documentType: Document.Type, @ContentBuilder viewer: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

## Discussion

The current document for a given editor instance is also provided as an environment object for its subhierarchy.

- See Also: `CFBundleTypeRole` with a value of “Viewer”

## Parameters

- `documentType`: The type of document being viewed.
- `viewer`: The viewing UI for the provided document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:viewer:)-1rgjv)*
# init(newDocument:editor:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a document group that is able to create and edit reference file documents.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Create a DocumentGroup with an object conforming to Document protocol instead.

## Declaration

```swift
@preconcurrency
nonisolated init(newDocument: @escaping @Sendable () -> Document, @ContentBuilder editor: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content)
```

Available when `Document` conforms to `ReferenceFileDocument` and `Content` conforms to `View`.

**Other overloads**:

```swift
@preconcurrency
nonisolated init(newDocument: @autoclosure @escaping @Sendable () -> Document, @ContentBuilder editor: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

## Discussion

The current document for a given editor instance is also provided as an environment object for its subhierarchy.

Undo support is not automatically provided for this construction of a `DocumentGroup`, and any updates to the document by the editor view hierarchy are expected to register undo operations when appropriate.

## Parameters

- `newDocument`: The initial document used when the user creates a new document. The argument should create a new instance, such that a new document is created on each invocation of the closure.
- `editor`: The editing UI for the provided document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(newdocument:editor:)-1mltk)*